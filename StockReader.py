import numpy as np
import pandas as pd

class StockReader:

    def read_stocks(self, df):
        try:
            all_data = pd.read_csv(df)
            list_of_stocks = all_data["Symbol"].tolist()
            return list_of_stocks
        except:
            return "An error has occured"

    def stock_exists(self, stock_name, df):
        if stock_name in self.read_stocks(df):
            return True
        else:
            return False

