import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

    def calculate_statistics(self):
        # Calculating statistics for 价格(元/月) and 单位面积价格(元/平米/月)
        price_stats = self.data["价格(元/月)"].describe(percentiles=[0.5])
        unit_price_stats = self.data["单位面积价格(元/平米/月)"].describe(percentiles=[0.5])

        # Extracting required statistics
        self.price_summary = {
            "价格均价": int(price_stats["mean"]),
            "价格最高价": int(price_stats["max"]),
            "价格最低价": int(price_stats["min"]),
            "价格中位数": int(price_stats["50%"]),
        }

        self.unit_price_summary = {
            "单位面积价格均价": round(unit_price_stats["mean"], 2),
            "单位面积价格最高价": round(unit_price_stats["max"], 2),
            "单位面积价格最低价": round(unit_price_stats["min"], 2),
            "单位面积价格中位数": round(unit_price_stats["50%"], 2),
        }

    def get_price_summary(self):
        return self.price_summary

    def get_unit_price_summary(self):
        return self.unit_price_summary


if __name__ == "__main__":
    # Example usage:
    analyzer = DataAnalyzer("data/bj.csv")
    analyzer.calculate_statistics()
    print(analyzer.get_price_summary())
    print(analyzer.get_unit_price_summary())
