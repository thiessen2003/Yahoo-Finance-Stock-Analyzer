import unittest
from StockReader import StockReader

class TestStockReader(unittest.TestCase):

    def setUp(self):
        self.stock_tester = StockReader()
        self.wrong_df = "../data/nullcsv.csv"
        self.right_df = "../data/stocklist.csv"

    def test_read_stocks_valid(self):
        stocks = self.stock_tester.read_stocks(self.right_df)
        self.assertGreater(len(stocks), 0)

    def test_stock_exists_true(self):
        exists = self.stock_tester.stock_exists("AAPL", self.right_df)
        self.assertTrue(exists)

    def test_stock_exists_false(self):
        exists = self.stock_tester.stock_exists("FAKESTOCK", self.right_df)
        self.assertFalse(exists)


if __name__ == "__main__":
    unittest.main()
