from copy import deepcopy as dc
from torch.utils.data import Dataset
import torch
import torch.nn as nn

def prepare_dataframe_for_lstm(df, sequence_length):
    df = dc(df)

    df.set_index('date', inplace=True)

    for i in range(1, sequence_length+1):
        df[f'close(d-{i})'] = df['close'].shift(i)

    df.dropna(inplace=True)
    
    return df

class TimeSeriesDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, i):
        return self.X[i], self.y[i]
    
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
