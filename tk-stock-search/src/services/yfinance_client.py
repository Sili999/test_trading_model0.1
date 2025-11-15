import yfinance as yf

def get_stock_info(ticker_symbol, fields):
    """
    Fetch stock information for a given ticker symbol.
    
    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL')
        fields (list): List of fields to retrieve
    
    Returns:
        dict: Dictionary with requested fields and their values
    
    Raises:
        Exception: If the ticker symbol is invalid or network error occurs
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        result = {field: info.get(field, None) for field in fields}
        return result
    except Exception as e:
        raise Exception(f"Error fetching stock info for {ticker_symbol}: {str(e)}")