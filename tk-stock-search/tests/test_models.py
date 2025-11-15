import unittest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models.stock import Stock

class TestStockModel(unittest.TestCase):

    def setUp(self):
        self.stock = Stock(ticker="AAPL", name="Apple Inc.", market_cap=2500000000000, previous_close=150.00)

    def test_stock_initialization(self):
        self.assertEqual(self.stock.ticker, "AAPL")
        self.assertEqual(self.stock.name, "Apple Inc.")
        self.assertEqual(self.stock.market_cap, 2500000000000)
        self.assertEqual(self.stock.previous_close, 150.00)

    def test_market_cap_formatting(self):
        self.assertEqual(self.stock.get_market_cap_formatted(), "2.5 Trillion")

    def test_previous_close(self):
        self.assertEqual(self.stock.get_previous_close(), 150.00)

if __name__ == '__main__':
    unittest.main()