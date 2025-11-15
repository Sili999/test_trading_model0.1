import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services.yfinance_client import get_stock_info

class TestYFinanceClient(unittest.TestCase):

    def test_get_stock_info_valid_ticker(self):
        fields = ['shortName', 'sector', 'marketCap', 'previousClose']
        stock_info = get_stock_info('AAPL', fields)
        self.assertIsNotNone(stock_info)
        self.assertIn('shortName', stock_info)
        self.assertIn('sector', stock_info)
        self.assertIn('marketCap', stock_info)
        self.assertIn('previousClose', stock_info)

    def test_get_stock_info_invalid_ticker(self):
        fields = ['shortName', 'sector', 'marketCap', 'previousClose']
        stock_info = get_stock_info('INVALID_TICKER', fields)
        self.assertIsNotNone(stock_info)
        self.assertEqual(stock_info['shortName'], None)

if __name__ == '__main__':
    unittest.main()