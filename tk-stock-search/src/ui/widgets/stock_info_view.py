import tkinter as tk
from tkinter import ttk
import yfinance as yf

class StockInfoView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_ticker = None
        self.create_widgets()

    def create_widgets(self):
        self.stock_label = ttk.Label(self, text="Stock Information", font=("Helvetica", 16, "bold"))
        self.stock_label.pack(pady=10)

        # Create a scrollbar and text widget
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.info_text = tk.Text(self, wrap=tk.WORD, height=20, width=80, yscrollcommand=scrollbar.set)
        self.info_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.info_text.yview)

        # Button frame
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        self.refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_current)
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_info)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def refresh_current(self):
        """Refresh the current ticker"""
        if self.current_ticker:
            self.refresh_info(self.current_ticker)

    def refresh_info(self, ticker_symbol):
        """Fetch and display stock info for a given ticker"""
        try:
            self.current_ticker = ticker_symbol
            stock_info = self.get_stock_info(ticker_symbol)
            self.display_info(stock_info)
        except Exception as e:
            self.display_error(f"Error fetching data: {str(e)}")

    def get_stock_info(self, ticker_symbol):
        """Get stock information from yfinance"""
        try:
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info
            fields = ['shortName', 'sector', 'marketCap', 'previousClose', 'currentPrice', 
                     'dividendYield', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'trailingPE']
            result = {field: info.get(field, 'N/A') for field in fields}
            return result
        except Exception as e:
            raise Exception(f"Failed to fetch stock info: {str(e)}")

    def display_info(self, stock_info):
        """Display stock information in the text widget"""
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, f"Ticker: {self.current_ticker.upper()}\n")
        self.info_text.insert(tk.END, "=" * 50 + "\n\n")
        
        for key, value in stock_info.items():
            formatted_key = key.replace('_', ' ').title()
            self.info_text.insert(tk.END, f"{formatted_key}: {value}\n")

    def display_error(self, error_message):
        """Display error message"""
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, f"Error: {error_message}", "error")
        self.info_text.tag_config("error", foreground="red")

    def clear_info(self):
        """Clear the info display"""
        self.info_text.delete(1.0, tk.END)
        self.current_ticker = None