# Creating a stock network tracker using stock data and Python
import yfinance as yf
import pandas as pd

tickers = ["AMZN", "AAPL", "GOOGL", "MSFT", "TSLA"]
print(tickers)

market_data = yf.download(tickers, start="2026-08-01", end="2026-09-01")
print(market_data)
