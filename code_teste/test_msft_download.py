import yfinance as yf

# Define o ticker
symbol = "MSFT"

# Obtém todos os dados históricos disponíveis
data = yf.download(symbol)

# Exibe os dados
print(data)
