import tkinter as tk
from tkinter import ttk, messagebox
from .widgets.search_bar import SearchBar
from .widgets.stock_info_view import StockInfoView
from .widgets.market_indicators_view import MarketIndicatorsView

class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Stock Search Application")
        self.root.geometry("1000x700")

        self.create_widgets()

    def create_widgets(self):
        # Create a main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create and pack the market indicators view at the top
        self.market_indicators_view = MarketIndicatorsView(main_frame)
        self.market_indicators_view.pack(fill=tk.X, pady=(0, 10))

        # Create separator
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

        # Create and pack the search bar
        self.search_bar = SearchBar(main_frame, search_callback=self.on_search)
        self.search_bar.pack(fill=tk.X, pady=10)

        # Create and pack the stock info view
        self.stock_info_view = StockInfoView(main_frame)
        self.stock_info_view.pack(fill=tk.BOTH, expand=True, pady=10)

    def on_search(self, ticker):
        """Handle search callback from search bar"""
        try:
            self.stock_info_view.refresh_info(ticker)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch stock info for {ticker}: {str(e)}")

if __name__ == "__main__":
    app = MainWindow(tk.Tk())
    app.pack(fill=tk.BOTH, expand=True)
    app.mainloop()