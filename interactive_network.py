"""Creating an interactive stock network tracker"""

import streamlit as st
import yfinance as yf
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.title("Stock Network Tracker")

user_tickers = st.text_input("Enter stock tickers separated by commas (ex: AMZN, AAPL, GOOGL):", "AAPL, MSFT, GOOGL, AMZN, TSLA")

tickers_list = [ticker.strip() for ticker in user_tickers.split(",") if ticker.strip()]

threshold = st.slider("Select correlation threshold:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

st.write(f"Selected tickers: {user_tickers}")
st.write(threshold)

if len(tickers_list) >= 2:
    market_data = yf.download(tickers_list, start="2026-08-01", end="2026-09-01")

    closing_prices = market_data['Close']
    daily_returns = closing_prices.pct_change()
    correlation_matrix = daily_returns.corr()

    edges = []

    for i in range(len(correlation_matrix)):
        for j in range(i):
            stock1 = correlation_matrix.columns[i]
            stock2 = correlation_matrix.columns[j]
            correlation = correlation_matrix.iloc[i,j]

            if abs(correlation) > threshold:
                edges.append((stock1, stock2, correlation))

    edge_weights = []
    for stock1, stock2, corr in edges:
        edge_weights.append(corr * 5)

    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, k=0.5)

    fig, ax = plt.subplots(figsize=(10, 8))

    nx.draw(G, pos, with_labels=True, width=edge_weights, ax=ax)

    st.pyplot(fig)

else:
    st.warning("Please enter at least two stock tickers to generate a network.")