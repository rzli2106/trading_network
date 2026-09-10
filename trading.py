# Creating a stock network tracker using stock data and Python
import yfinance as yf
import pandas as pd

tickers = ["AMZN", "AAPL", "GOOGL", "MSFT", "TSLA"]
print(tickers)

market_data = yf.download(tickers, start="2026-08-01", end="2026-09-01")
print(market_data)

closing_prices = market_data['Close']
daily_returns = closing_prices.pct_change()


#using pandas to calculate the correlation matrix
correlation_matrix = daily_returns.corr()
print(correlation_matrix)

threshold = 0.3
edges = []

for i in range(len(correlation_matrix)):
    for j in range(i):
        stock1 = correlation_matrix.columns[i]
        stock2 = correlation_matrix.columns[j]
        coorelation = correlation_matrix.iloc[i,j]

        if abs(correlation) > threshold:
            edges.append((stock1, stock2, correlation))

print(edges)

