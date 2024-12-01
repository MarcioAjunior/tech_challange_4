import torch
import os
from lstm import LSTM


class Model:
    def __init__(self,model_path,db_config, ticker):
        self.model = None    
        self.model_path = model_path
        self.db_config = db_config
        self.ticker = ticker

    def load_model(self):
        if self.model is None:
            if os.path.exists(self.model_path):
                print("carregando...")
                self.model = LSTM()
                checkpoint = torch.load("model.pth", map_location=self.model.device)
                self.model.load_state_dict(checkpoint['model_state_dict'])
            else:
                self.model = LSTM()
                
    def predict(self, date=''):      
        self.load_model()
        
        predictions = self.model.predict(
            target_date=str(date),
            ticker=self.ticker,
            db_config=self.db_config,
            sequence_length=7
        )
        
        return predictions
