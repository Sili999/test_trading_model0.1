import yfinance as yf

def get_stock_info(ticker_symbol, fields):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    result = {field: info.get(field, None) for field in fields}
    return result

def get_interest_rates():
    # Placeholder for fetching current interest rates
    # This function should be implemented to retrieve real-time data
    return {"current_interest_rate": "2.5%"}

def get_us_bonds_info():
    # Placeholder for fetching US bonds information
    # This function should be implemented to retrieve real-time data
    return {"10_year_bond": "1.75%", "30_year_bond": "2.00%"}