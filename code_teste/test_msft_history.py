import yfinance as yf

# Define o ticker
ticker = yf.Ticker("MSFT")

# Obtém todos os dados históricos
history = ticker.history(period="max")

# Exibe os dados
print(history)
