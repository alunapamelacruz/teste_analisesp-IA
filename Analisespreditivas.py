# Análises preditivas

## Carregando dados

!pip install yfinance
import yfinance
ticker = input("Digite o ticker da ação desejada: ")

acao = yfinance.Ticker(ticker).history(2y)
acao.Close.plot()
