import pandas as pd


def alter_data(path):
    data = pd.read_csv(path)
    data["单位面积价格(元/平米/月)"] = round(data["价格(元/月)"] / data["面积(平米)"], 2)
    data.to_csv(path, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    alter_data("data/bj.csv")
    alter_data("data/sh.csv")
    alter_data("data/gz.csv")
    alter_data("data/sz.csv")
    alter_data("data/cd.csv")
