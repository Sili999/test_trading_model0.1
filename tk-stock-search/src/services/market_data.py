import yfinance as yf

def get_interest_rates():
    """
    Fetch current interest rates.
    Uses Treasury yields as proxy for interest rates.
    
    Returns:
        dict: Dictionary containing interest rate data
    """
    try:
        treasury = yf.Ticker("^IRX")
        fed_rate = treasury.info.get("currentPrice", "N/A")
        return {
            "Federal Funds Rate": f"{fed_rate}%" if fed_rate != "N/A" else "N/A"
        }
    except Exception as e:
        return {"Federal Funds Rate": "N/A"}

def get_bond_info():
    """
    Fetch US bond information including yields and prices.
    
    Returns:
        dict: Dictionary containing bond data
    """
    try:
        bond_10y = yf.Ticker("^TNX")
        bond_30y = yf.Ticker("^TYX")
        
        yield_10y = bond_10y.info.get("currentPrice", "N/A")
        yield_30y = bond_30y.info.get("currentPrice", "N/A")
        
        return {
            "US 10-Year Bond": {
                "Yield": f"{yield_10y}%" if yield_10y != "N/A" else "N/A"
            },
            "US 30-Year Bond": {
                "Yield": f"{yield_30y}%" if yield_30y != "N/A" else "N/A"
            }
        }
    except Exception as e:
        return {
            "US 10-Year Bond": {"Yield": "N/A"},
            "US 30-Year Bond": {"Yield": "N/A"}
        }

def get_market_data():
    """
    Get all market data including interest rates and bond information.
    
    Returns:
        dict: Dictionary containing all market indicators
    """
    try:
        interest_rates = get_interest_rates()
        bond_info = get_bond_info()
        return {
            "interest_rates": interest_rates,
            "bond_info": bond_info
        }
    except Exception as e:
        return {
            "error": f"Failed to fetch market data: {str(e)}"
        }