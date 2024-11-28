import mlflow.pytorch

class Model:
    def __init__(self,tracking_uri, model_uri, db_config, ticker):
        self.model = None    
        self.tracking_uri = tracking_uri
        self.model_uri = model_uri
        self.db_config = db_config
        self.ticker = ticker

    def __enter__(self):
        print('iniciando carregamento do modelo')        
        mlflow.set_tracking_uri(self.tracking_uri)
        self.model = mlflow.pytorch.load_model(self.model_uri)
        print("Modelo carregado.")
        return self

    

    def __exit__(self, exc_type, exc_value, traceback):

        self.model = None
        print("Modelo descarregado.")

    def predict(self, date=''):
        with self:
            if self.model is None:
                raise RuntimeError("Modelo não carregado.")
            
            date = "2024-12-01"
            print(date)
            predictions = self.model.predict(date, self.db_config, self.ticker)
            print('predict return = ', predictions)
            return predictions
