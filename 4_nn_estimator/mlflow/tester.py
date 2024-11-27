import torch
import numpy as np
from lstm import LSTM

input_size = 1 
hidden_size = 4 
num_layers = 1
sequence_length = 7

db_config = {
    "host": "localhost",
    "port": "5434",
    "dbname": "db",
    "user": "user",
    "password": "password"
}

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
model = LSTM(input_size, hidden_size, num_layers, device)
model.to(device)

predictions = model.predict(
    target_date='2024-12-01',
    ticker='MSFT',
    db_config=db_config,
    sequence_length=sequence_length
)

print(predictions)
