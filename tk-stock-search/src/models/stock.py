class Stock:
    def __init__(self, ticker=None, ticker_symbol=None, name=None, short_name=None, sector=None, market_cap=None, previous_close=None):
        # Support both old and new parameter names for backwards compatibility
        self.ticker = ticker or ticker_symbol
        self.ticker_symbol = self.ticker
        self.name = name or short_name
        self.short_name = self.name
        self.sector = sector
        self.market_cap = market_cap
        self.previous_close = previous_close

    def __repr__(self):
        return f"Stock(ticker={self.ticker}, name={self.name}, sector={self.sector}, market_cap={self.market_cap}, previous_close={self.previous_close})"

    def get_summary(self):
        return {
            "Ticker Symbol": self.ticker,
            "Name": self.name,
            "Sector": self.sector,
            "Market Cap": self.market_cap,
            "Previous Close": self.previous_close
        }

    def get_market_cap_formatted(self):
        """Format market cap into human-readable format"""
        if self.market_cap is None:
            return "N/A"
        
        market_cap = float(self.market_cap)
        if market_cap >= 1e12:
            return f"{market_cap / 1e12:.1f} Trillion"
        elif market_cap >= 1e9:
            return f"{market_cap / 1e9:.1f} Billion"
        elif market_cap >= 1e6:
            return f"{market_cap / 1e6:.1f} Million"
        else:
            return f"{market_cap:.0f}"

    def get_previous_close(self):
        """Get the previous close price"""
        return self.previous_close