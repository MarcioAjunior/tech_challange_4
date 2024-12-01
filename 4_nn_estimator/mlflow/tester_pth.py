import torch
import numpy as np
from generate_model_pth import LSTM
import joblib  # Para carregar o scaler

# Configurações do modelo e entrada
input_size = 1 
hidden_size = 4 
num_layers = 1
sequence_length = 7
saved_model_path = "model_checkpoint.pth" 

db_config = {
    "host": "localhost",
    "port": "5434",
    "dbname": "db",
    "user": "user",
    "password": "password"
}

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

model = LSTM(input_size, hidden_size, num_layers, device)

checkpoint = torch.load("model.pth", map_location=device)

model.load_state_dict(checkpoint['model_state_dict'])

predictions = model.predict(
    target_date='2024-12-10',
    ticker='MSFT',
    db_config=db_config,  # Retirado porque os dados vêm diretamente
    sequence_length=sequence_length
)

print(predictions)
