from database import Db
import os
from dotenv import load_dotenv
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import numpy as np
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.pytorch
from copy import deepcopy as dc
from lstm import prepare_dataframe_for_lstm, TimeSeriesDataset, LSTM

load_dotenv()

os.getenv("FROM_DATE")

FROM_DATE =  os.getenv("FROM_DATE") if os.getenv("FROM_DATE") != 'None' else None 
TICKER = os.getenv("TICKER")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

def create_lstm_data(data, sequence_length, index):
    x, y = [], []
    for i in range(len(data) - sequence_length):
        x.append(data[i:(i + sequence_length), :]) 
        y.append(data[i + sequence_length, index])
    return np.array(x), np.array(y)

if __name__ == '__main__':
    
    #Buscando no banco de dados
    conn = Db(db_config = DB_CONFIG) 
    tickers_data = conn.get_data_tickers(FROM_DATE, ticker=TICKER)
    df = pd.DataFrame(data=tickers_data)

    
    #Redefinindo meu dataframe
    data = df[['date', 'close']]
    
    print(data.head())
    
    #Setando device
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
    
    mlflow.set_experiment("LSTM Artificial Data Regression 2")
    
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

        print("Modelo salvo com normalizador incluído!")
