import os
from dotenv import load_dotenv
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
import torch.nn as nn
import numpy as np
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.pytorch
from copy import deepcopy as dc
import psycopg2
from psycopg2.extras import execute_values

load_dotenv()


FROM_DATE =  os.getenv("FROM_DATE") if os.getenv("FROM_DATE") != 'None' else None 

print(FROM_DATE, 'FROM_DATE')

TICKER = os.getenv("TICKER")

print(TICKER, 'TICKER')

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

print(DB_CONFIG, 'DB_CONFIG')

def prepare_dataframe_for_lstm(df, sequence_length):
    df = dc(df)

    df.set_index('date', inplace=True)

    for i in range(1, sequence_length+1):
        df[f'close(d-{i})'] = df['close'].shift(i)

    df.dropna(inplace=True)
    
    return df

#class Db
class Db:
    _instance = None
    _config = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._config = kwargs.get("db_config")
            cls._instance.init_connection(kwargs.get("db_config"))
            
        return cls._instance

    def init_connection(self, db_config):
        if not db_config:
            raise ValueError("configuração do banco incorreta")
        
        self.connection = psycopg2.connect(**db_config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            
    def get_data_tickers(self, from_date = None, ticker = None):
        
        self.connection = psycopg2.connect(**self._config)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        
        query = f"""
            SELECT 
                ticker
                ,open
                ,high
                ,low
                ,close
                ,volume
                ,date
            FROM
                lb_tickers_data
            WHERE
                ticker = '{ticker}'
            order by
                date
            """
        
        if from_date is not None:
            query = f"""
            SELECT 
                ticker
                ,open
                ,high
                ,low
                ,close
                ,volume
                ,date
            FROM 
                lb_tickers_data
            WHERE
                cast(date as date) > cast('{from_date}' as date)
                and ticker = '{ticker}'
            ORDER BY
                date 
            """        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            
            results = [{
                "ticker" : item[0]
                ,"open" : item[1]
                ,"high" : item[2]
                ,"low" : item[3]
                ,"close" : item[4]
                ,"volume" : item[5]
                ,"date" : item[6]
                } for item in results] 
            
            return results
        except Exception as e:
            print(f"Erro ao buscada dados do ticker: {e}")
        finally:
            self.close_connection()

#Classe LSTM
class LSTM(nn.Module):
    def __init__(self, input_size = 1, hidden_size = 4, num_layers = 1 , sequence_length = 7, porcentage_train = 0.95, batch_size = 16, learning_rate = 0.001,num_epochs = 10, device='cpu'):
        super().__init__()
        self.input_size = 1 
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.sequence_length = sequence_length
        self.porcentage_train = porcentage_train
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.device = device

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True)

        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        batch_size = x.size(0)
        h0 = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(self.device)
        c0 = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(self.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out
    
    def predict(self, target_date, db_config, ticker='', sequence_length=7):
        from sklearn.preprocessing import MinMaxScaler
        from database import Db
        import pandas as pd
        import numpy as np
        import datetime
        import torch
        
        # Configurando o scaler e carregando dados
        scaler = MinMaxScaler(feature_range=(-1, 1))
        from_date = datetime.datetime.now() - datetime.timedelta(days=sequence_length)
        from_date_str = from_date.strftime('%Y-%m-%d')
        
        conn = Db(db_config=db_config)
        tickers_data = conn.get_data_tickers(None, ticker=ticker)
        
        df = pd.DataFrame(data=tickers_data)
        
        # Preparando o DataFrame para o modelo
        historical_data = df[['date', 'close']].sort_values(by='date', ascending=False)
        
        historical_data.dropna(inplace=True)
                
        prepared_df = prepare_dataframe_for_lstm(historical_data, sequence_length=sequence_length)
        
        prepared_df = prepared_df.head(sequence_length)
        
        prepared_df_np = prepared_df.to_numpy()
        
        # Normalizando os dados
        prepared_df_np = scaler.fit_transform(prepared_df_np)
        X_input_normalized = prepared_df_np[:, 1:]  
        X_input_normalized = np.flip(X_input_normalized, axis=1)  
        X_input_normalized = X_input_normalized.reshape((-1, sequence_length, 1))  
                
        X_input_tensor = torch.tensor(X_input_normalized.copy()).float().to(self.device)

        current_date = historical_data['date'].max()  # Última data registrada
        current_date += datetime.timedelta(days=1)
        if hasattr(current_date, 'tzinfo') and current_date.tzinfo is not None:
            current_date = current_date.replace(tzinfo=None)

        target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").replace(tzinfo=None)

        dates_to_predict = pd.date_range(start=current_date, end=target_date).strftime('%Y-%m-%d').tolist()

        new_sequence = X_input_normalized[-1, :]
        predictions = []
        self.eval()
        
        for date in dates_to_predict:  
            with torch.no_grad():
                X_input_tensor = torch.tensor(new_sequence.reshape((1, sequence_length, 1)).copy()).float().to(self.device)

                predicted = self(X_input_tensor)
                
            predicted_value = predicted.cpu().numpy().reshape(1, -1) 
            
            predicted_value_with_dummy_columns = np.zeros((predicted_value.shape[0], 8)) 
            predicted_value_with_dummy_columns[:, 0] = predicted_value.flatten()

            predicted_value_corrected = scaler.inverse_transform(predicted_value_with_dummy_columns)

            predicted_value_final = predicted_value_corrected[:, 0]
            
            new_sequence = np.roll(new_sequence, -1)  
            new_sequence[-1] = predicted_value_final.flatten()[0] 

            #print(new_sequence)

            predictions.append({
                'date': date,
                'predicted_close': predicted_value_final.flatten()[0]
            })
            
            
        return predictions
    
class TimeSeriesDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, i):
        return self.X[i], self.y[i]

if __name__ == '__main__':
    
    #Buscando no banco de dados
    conn = Db(db_config = DB_CONFIG) 
    tickers_data = conn.get_data_tickers(FROM_DATE, ticker=TICKER)
    df = pd.DataFrame(data=tickers_data)
    
    #Redefinindo meu dataframe
    data = df[['date', 'close']]
    
    print(data.head(), 'DATA HEAD')
    
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    
    model = LSTM(
        input_size=1,
        hidden_size = 4,
        num_layers = 1,
        sequence_length=7,
        porcentage_train = 0.95,
        batch_size = 16,
        learning_rate = 0.001,
        num_epochs = 10,
        device=device)
    
    model.to(device)
    
    #Preparando dados para o modelo LSTM
    prepared_df = prepare_dataframe_for_lstm(data, model.sequence_length)
    prepared_df_np = prepared_df.to_numpy()
    
    #Normalizando os valores do dataset
    scaler = MinMaxScaler(feature_range=(-1, 1))
    prepared_df_np = scaler.fit_transform(prepared_df_np)
    
    #Definindo treino e teste 
    X = prepared_df_np[:, 1:]
    X = dc(np.flip(X, axis=1))

    y = prepared_df_np[:, 0]
    
    train_size = int(len(X) * model.porcentage_train)
    
    X_train = X[:train_size]
    X_test = X[train_size:]

    y_train = y[:train_size]
    y_test = y[train_size:]
    
    #Preparando dimensão extra para o modelo LSTM do pythorch
    X_train = X_train.reshape((-1, model.sequence_length, 1))
    X_test = X_test.reshape((-1, model.sequence_length, 1))
    
    y_train = y_train.reshape((-1, 1))
    y_test = y_test.reshape((-1, 1))
    
    #Criando tensores com meu X e Y train test
    X_train = torch.tensor(X_train).float()
    y_train = torch.tensor(y_train).float()
    X_test = torch.tensor(X_test).float()
    y_test = torch.tensor(y_test).float()
    
    #Criando os datasets temportais e dataLoaders
    train_dataset = TimeSeriesDataset(X_train, y_train)
    test_dataset = TimeSeriesDataset(X_test, y_test)
    train_loader = DataLoader(train_dataset, batch_size=model.batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=model.batch_size, shuffle=False)
    
    #Definido critério otimizador
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), model.learning_rate)
    
    mlflow.set_experiment("LSTM Artificial Data Regression 4")
    
    with mlflow.start_run():
        
        mlflow.log_param(f"sequence_length",model.sequence_length)
        mlflow.log_param(f"porcentage_train",model.porcentage_train)
        mlflow.log_param(f"batch_size",model.batch_size)
        mlflow.log_param(f"input_size",model.input_size)
        mlflow.log_param(f"hidden_size",model.hidden_size)
        mlflow.log_param(f"num_layers",model.num_layers)
        mlflow.log_param(f"learning_rate",model.learning_rate)
        mlflow.log_param(f"num_epochs",model.num_epochs)
        
        #Treinando e validando modelo por epocas
        for epoch in range(model.num_epochs):
            #Trieno
            model.train(True)
            print(f'Epoch: {epoch + 1}')
            epoch_train_loss = 0.0
            y_true_train, y_pred_train = [], []
            
            for batch_index, batch in enumerate(train_loader):
                x_batch, y_batch = batch[0].to(device), batch[1].to(device)

                output = model(x_batch)
                loss = loss_function(output, y_batch)
                epoch_train_loss += loss.item()
                
                # Armazenando valores para cálculo do MSE
                y_true_train.extend(y_batch.cpu().numpy().flatten())
                y_pred_train.extend(output.cpu().detach().numpy().flatten())

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                if batch_index % 100 == 99:
                    avg_loss_batchs = epoch_train_loss / 100
                    print('Batch {0}, Loss: {1:.3f}'.format(batch_index+1, avg_loss_batchs))
                    epoch_train_loss = 0.0
            
            mse_train = mean_squared_error(y_true_train, y_pred_train)
            print(f'train_mse {round(mse_train, 4)}')
            
            print('\n')
            print('##')
                    
            #Validação
            model.eval()
            epoch_val_loss = 0.0
            y_true_val, y_pred_val = [], []
            
            for batch_index, batch in enumerate(test_loader):
                x_batch, y_batch = batch[0].to(device), batch[1].to(device)

                with torch.no_grad():
                    output = model(x_batch)
                    loss = loss_function(output, y_batch)
                    epoch_val_loss += loss.item()
                    
                    y_true_val.extend(y_batch.cpu().numpy().flatten())
                    y_pred_val.extend(output.cpu().numpy().flatten())
                    
            # Calculando o MSE para a validação na época atual
            mse_val = mean_squared_error(y_true_val, y_pred_val)
            print(f'val_mse = {mse_val}')
            mlflow.log_metric("val_mse", mse_val, step=epoch)
            
            # Média da perda 
            avg_loss_batchs = epoch_val_loss / len(test_loader)
            print(f'avg_loss_batchs = {avg_loss_batchs}')
            mlflow.log_metric("val_avg_loss", avg_loss_batchs, step=epoch)
            
        # Salvando no MLflow
        mlflow.pytorch.log_model(
            pytorch_model=model,
            artifact_path="wrapped_lstm_model_with_scaler",
            registered_model_name="LSTM_with_scaler"
        )

        print("Modelo salvo")