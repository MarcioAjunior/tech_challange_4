from database import Db
import os
from dotenv import load_dotenv
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import numpy as np
import torch.optim as optim
from sklearn.metrics import mean_absolute_error
import mlflow
import mlflow.pytorch

load_dotenv()

os.getenv("FROM_DATE")

#UMA DATA QUE PODE SER USADA PARA SELECIONAR DADOS A PARTIR DE UMA DATA, QUANDO None PEGA TODOS OS DADOS
FROM_DATE =  os.getenv("FROM_DATE") if os.getenv("FROM_DATE") != 'None' else None 

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
    tickers_data = conn.get_data_tickers(FROM_DATE)
    df = pd.DataFrame(data=tickers_data)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    #Definindo hiperparâmetros
    columns = ['close']
    
    input_size = len(columns)    # Number of features in the input data
    index_target = input_size - 1
    
    hidden_size = 32     # Number of hidden units in the LSTM
    num_layers = 4       # Number of LSTM layers
    output_size = 1      # Number of output units (e.g., regression output)
    num_epochs = 100
    batch_size = 64
    learning_rate = 0.001
    sequence_length = 30  # Length of the input sequences

    df = df.sort_values('date')
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    data = df[columns].values

    #scaler = MinMaxScaler()
    #data_scaled = scaler.fit_transform(data)
    
    X, y = create_lstm_data(data, sequence_length,index_target)
    
    train_size = int(0.8 * len(X))
    X_train, y_train = X[:train_size], y[:train_size]
    X_test, y_test = X[train_size:], y[train_size:]
    
    # Conversão para tensores
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(device)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).to(device)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).to(device)
    
    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    class LSTM(nn.Module):
        
        def __init__(self, input_size, hidden_size, num_layers, output_size):
            super(LSTM, self).__init__()
            self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
            self.fc = nn.Linear(hidden_size, output_size)

        def forward(self, x):
            out, _ = self.lstm(x)
            out = self.fc(out[:, -1, :])
            return out
    
    def train_model():

        model = LSTM(input_size, hidden_size, num_layers, output_size).to(device)
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

        mlflow.set_experiment("LSTM Artificial Data Regression")
        with mlflow.start_run():
            """mlflow.log_param("intermediate_networks", [
                model.lstm.__name__,
                model.fc.__name__
            ])"""
            mlflow.log_param("input_size", input_size)
            mlflow.log_param("hidden_size", hidden_size)
            mlflow.log_param("num_layers", num_layers)
            mlflow.log_param("output_size", output_size)
            mlflow.log_param("num_epochs", num_epochs)
            mlflow.log_param("batch_size", batch_size)
            mlflow.log_param("learning_rate", learning_rate)
            mlflow.log_param("sequence_length", sequence_length)

            for epoch in range(num_epochs):
                model.train()
                running_loss = 0.0
                
                for i, (sequences, labels) in enumerate(train_loader):
                    sequences, labels = sequences.to(device), labels.to(device)

                    # Forward pass
                    outputs = model(sequences)
                    loss = criterion(outputs, labels)

                    # Backward pass and optimization
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                    running_loss += loss.item()
                    
                    # Log metrics every 100 batches
                    if i % 100 == 0:
                        print(f"Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}")
                        mlflow.log_metric("train_loss", running_loss / (i+1), step=epoch * len(train_loader) + i)

            # Save the model
            mlflow.pytorch.log_model(model, "lstm_artificial_data_model")

            # Evaluate the model
            evaluate_model(model, criterion)
            
    def evaluate_model(model, criterion):
        model.eval()
        test_loss = 0.0
        predictions = []
        true_values = []
        
        with torch.no_grad():
            for sequences, labels in test_loader:
                sequences, labels = sequences.to(device), labels.to(device)
                outputs = model(sequences)
                loss = criterion(outputs, labels)
                test_loss += loss.item()
                
                predictions.extend(outputs.cpu().numpy())
                true_values.extend(labels.cpu().numpy())

        #MSE
        average_test_loss = test_loss / len(test_loader)
        print(f"Test Loss: {average_test_loss:.4f}")
        mlflow.log_metric("test_loss", average_test_loss)
        
        #MAE
        mae = mean_absolute_error(true_values, predictions)
        print(f"Mean Absolute Error: {mae:.4f}")
        mlflow.log_metric("mae", mae)
        
    train_model()