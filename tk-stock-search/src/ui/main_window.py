import tkinter as tk
from tkinter import ttk
from .widgets.search_bar import SearchBar
from .widgets.stock_info_view import StockInfoView
from .widgets.market_indicators_view import MarketIndicatorsView

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Search Application")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Create and pack the search bar
        self.search_bar = SearchBar(self)
        self.search_bar.pack(pady=10)

        # Create and pack the stock info view
        self.stock_info_view = StockInfoView(self)
        self.stock_info_view.pack(pady=10)

        # Create and pack the market indicators view
        self.market_indicators_view = MarketIndicatorsView(self)
        self.market_indicators_view.pack(pady=10)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()