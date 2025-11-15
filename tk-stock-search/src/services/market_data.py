import yfinance as yf

def get_interest_rates():
    # Placeholder for fetching current interest rates
    # This could be replaced with actual data fetching logic
    return {
        "Federal Funds Rate": "0.25%",
        "10-Year Treasury Yield": "1.50%"
    }

def get_bond_info():
    # Placeholder for fetching US bond information
    # This could be replaced with actual data fetching logic
    return {
        "US 10-Year Bond": {
            "Yield": "1.50%",
            "Price": "$100.50"
        },
        "US 30-Year Bond": {
            "Yield": "2.00%",
            "Price": "$98.75"
        }
    }

def get_market_data():
    interest_rates = get_interest_rates()
    bond_info = get_bond_info()
    return {
        "interest_rates": interest_rates,
        "bond_info": bond_info
    }