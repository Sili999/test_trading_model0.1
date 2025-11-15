import tkinter as tk
from tkinter import ttk
import yfinance as yf

class StockInfoView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.stock_label = ttk.Label(self, text="Stock Information", font=("Helvetica", 16))
        self.stock_label.pack(pady=10)

        self.info_text = tk.Text(self, wrap=tk.WORD, height=15, width=50)
        self.info_text.pack(padx=10, pady=10)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_info)
        self.refresh_button.pack(pady=5)

    def refresh_info(self, ticker_symbol):
        stock_info = self.get_stock_info(ticker_symbol)
        self.display_info(stock_info)

    def get_stock_info(self, ticker_symbol):
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        fields = ['shortName', 'sector', 'marketCap', 'previousClose']
        result = {field: info.get(field, 'N/A') for field in fields}
        return result

    def display_info(self, stock_info):
        self.info_text.delete(1.0, tk.END)
        for key, value in stock_info.items():
            self.info_text.insert(tk.END, f"{key}: {value}\n")