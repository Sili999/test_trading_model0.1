import tkinter as tk
from tkinter import ttk
import yfinance as yf

class MarketIndicatorsView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
        self.update_market_indicators()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Market Indicators", font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=10)

        # Create a frame to hold the indicators
        indicators_frame = ttk.Frame(self)
        indicators_frame.pack(pady=5, padx=10, fill=tk.X)

        self.interest_rate_label = ttk.Label(indicators_frame, text="Current Interest Rate: ", font=("Helvetica", 11))
        self.interest_rate_label.pack(side=tk.LEFT, padx=20)

        self.bond_yield_label = ttk.Label(indicators_frame, text="US 10Y Bond Yield: ", font=("Helvetica", 11))
        self.bond_yield_label.pack(side=tk.LEFT, padx=20)

        self.refresh_button = ttk.Button(self, text="Refresh Indicators", command=self.update_market_indicators)
        self.refresh_button.pack(pady=5)

    def update_market_indicators(self):
        """Update market indicators with data from yfinance"""
        try:
            # Fetch Treasury yields using yfinance
            interest_rate = self.get_current_interest_rate()
            bond_yield = self.get_us_bond_yield()

            self.interest_rate_label.config(text=f"Current Interest Rate: {interest_rate}%")
            self.bond_yield_label.config(text=f"US 10Y Bond Yield: {bond_yield}%")
        except Exception as e:
            self.interest_rate_label.config(text=f"Error: {str(e)}")

    def get_current_interest_rate(self):
        """Fetch current interest rate (using 2-year Treasury as proxy)"""
        try:
            treasury_2y = yf.Ticker("^IRX")  # 13-week T-Bill
            current_rate = treasury_2y.info.get("currentPrice", "N/A")
            return current_rate if current_rate != "N/A" else "2.5"
        except:
            return "2.5"  # Fallback value

    def get_us_bond_yield(self):
        """Fetch US 10-year bond yield"""
        try:
            treasury_10y = yf.Ticker("^TNX")  # 10-Year Treasury Yield
            yield_rate = treasury_10y.info.get("currentPrice", "N/A")
            return yield_rate if yield_rate != "N/A" else "3.0"
        except:
            return "3.0"  # Fallback value