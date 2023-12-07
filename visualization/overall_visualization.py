from overall_DataAnalyzer import DataAnalyzer


class CityInfo:
    price_summary = {}
    unit_price_summary = {}

    def __init__(self, file_path):
        analyzer = DataAnalyzer(file_path)
        analyzer.calculate_statistics()
        self.price_summary = analyzer.get_price_summary()
        self.unit_price_summary = analyzer.get_unit_price_summary()


if __name__ == "__main__":
    BJ = CityInfo("data/bj.csv")
    SH = CityInfo("data/sh.csv")
    GZ = CityInfo("data/gz.csv")
    SZ = CityInfo("data/sz.csv")
    CD = CityInfo("data/cd.csv")
    print(BJ.price_summary)
    print(SH.price_summary)
    print(GZ.price_summary)
    print(SZ.price_summary)
    print(CD.price_summary)
    print(BJ.unit_price_summary)
    print(SH.unit_price_summary)
    print(GZ.unit_price_summary)
    print(SZ.unit_price_summary)
    print(CD.unit_price_summary)
