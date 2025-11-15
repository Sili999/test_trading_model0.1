# tk-stock-search

This project is a Tkinter-based application for searching stock information and displaying important market indicators. It allows users to input stock ticker symbols and retrieve relevant data from the Yahoo Finance API.

## Project Structure

```
tk-stock-search
├── src
│   ├── main.py                # Entry point of the application
│   ├── app.py                 # Main application logic
│   ├── ui                     # User interface components
│   │   ├── __init__.py
│   │   ├── main_window.py      # Main window layout and initialization
│   │   └── widgets             # UI widgets
│   │       ├── search_bar.py   # Search bar for stock ticker input
│   │       ├── stock_info_view.py # Displays stock information
│   │       └── market_indicators_view.py # Displays market indicators
│   ├── services                # Services for data retrieval
│   │   ├── __init__.py
│   │   ├── yfinance_client.py   # Interacts with Yahoo Finance API
│   │   └── market_data.py       # Retrieves market data
│   ├── models                  # Data models
│   │   ├── __init__.py
│   │   └── stock.py            # Stock model definition
│   └── utils                   # Utility functions
│       ├── __init__.py
│       └── helpers.py          # Helper functions
├── tests                       # Unit tests
│   ├── test_yfinance_client.py  # Tests for yfinance_client functions
│   └── test_models.py           # Tests for Stock model
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files to ignore in version control
├── README.md                   # Project documentation
└── LICENSE                     # Licensing information
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd tk-stock-search
pip install -r requirements.txt
```

## Usage

Run the application by executing the following command:

```bash
python src/main.py
```

This will launch the Tkinter application, allowing you to search for stocks and view market indicators.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.