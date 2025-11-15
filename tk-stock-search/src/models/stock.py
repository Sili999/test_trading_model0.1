class Stock:
    def __init__(self, ticker_symbol, short_name, sector, market_cap, previous_close):
        self.ticker_symbol = ticker_symbol
        self.short_name = short_name
        self.sector = sector
        self.market_cap = market_cap
        self.previous_close = previous_close

    def __repr__(self):
        return f"Stock(ticker_symbol={self.ticker_symbol}, short_name={self.short_name}, sector={self.sector}, market_cap={self.market_cap}, previous_close={self.previous_close})"

    def get_summary(self):
        return {
            "Ticker Symbol": self.ticker_symbol,
            "Short Name": self.short_name,
            "Sector": self.sector,
            "Market Cap": self.market_cap,
            "Previous Close": self.previous_close
        }