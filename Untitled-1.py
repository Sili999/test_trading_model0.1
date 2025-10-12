import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def get_stock_info(ticker_symbol, fields):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    result = {field: info.get(field, None) for field in fields}
    return result

#Example usage:
'''fields = ['shortName', 'sector', 'marketCap', 'previousClose']
input_str = input("Zu welchen Aktien möchtest du Informationen? (Mehrere Ticker mit Semikolon trennen, z.B. AAPL;MSFT;GOOGL): ")
stocks = [s.strip() for s in input_str.split(';') if s.strip()]

for stock in stocks:
    stock_info = get_stock_info(stock, fields)
    print(f"{stock}: {stock_info}")'''
# --- IGNORE ---
#Apple info ordered by key
apple = yf.Ticker("AAPL")
apple_info = apple.info
for key in sorted(apple_info.keys()):
    print(f"{key}: {apple_info[key]}")