from overall_DataAnalyzer import DataAnalyzer
from matplotlib import pyplot as plt
import random


class CityInfo:
    price_summary = {}
    unit_price_summary = {}

    def __init__(self, file_path):
        analyzer = DataAnalyzer(file_path)
        analyzer.calculate_statistics()
        self.price_summary = analyzer.get_price_summary()
        self.unit_price_summary = analyzer.get_unit_price_summary()


if __name__ == "__main__":
    # 假设你有四个 DataAnalyzer 实例：analyzer1, analyzer2, analyzer3, analyzer4
    # 你需要首先对每个实例调用 calculate_statistics() 方法

    BJ = DataAnalyzer("data/bj.csv")
    SH = DataAnalyzer("data/sh.csv")
    GZ = DataAnalyzer("data/gz.csv")
    SZ = DataAnalyzer("data/sz.csv")
    CD = DataAnalyzer("data/cd.csv")

    BJ.calculate_statistics()
    SH.calculate_statistics()
    GZ.calculate_statistics()
    SZ.calculate_statistics()
    CD.calculate_statistics()

    # # 然后从每个实例中获取数据
    # price_summaries = [
    #     BJ.get_price_summary(),
    #     SH.get_price_summary(),
    #     GZ.get_price_summary(),
    #     SZ.get_price_summary(),
    #     CD.get_price_summary(),
    # ]

    # # 提取绘图所需的值
    # means = [summary["价格均价"] for summary in price_summaries]
    # maxes = [summary["价格最高价"] for summary in price_summaries]
    # mins = [summary["价格最低价"] for summary in price_summaries]
    # medians = [summary["价格中位数"] for summary in price_summaries]
    # categories = ["北京", "上海", "广州", "深圳", "成都"]
    # colors = [
    #     "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    #     for i in range(len(categories))
    # ]
    # plt.rcParams["font.sans-serif"] = ["SimHei"]
    # plt.rcParams["axes.unicode_minus"] = False

    # # 绘制均价条形图
    # plt.figure(figsize=(10, 6))
    # bars = plt.bar(categories, means, color=colors)
    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(
    #         bar.get_x() + bar.get_width() / 2, yval, int(yval), va="bottom", ha="center"
    #     )
    # plt.xlabel("城市")
    # plt.ylabel("均价 (元/月)")
    # plt.title("各城市房价均价对比")
    # plt.show()

    # # 绘制最高价条形图
    # plt.figure(figsize=(10, 6))
    # bars = plt.bar(categories, maxes, color=colors)
    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(
    #         bar.get_x() + bar.get_width() / 2, yval, int(yval), va="bottom", ha="center"
    #     )
    # plt.xlabel("城市")
    # plt.ylabel("最高价 (元/月)")
    # plt.title("各城市房价最高价对比")
    # plt.show()

    # # 绘制最低价条形图
    # plt.figure(figsize=(10, 6))
    # bars = plt.bar(categories, mins, color=colors)
    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(
    #         bar.get_x() + bar.get_width() / 2, yval, int(yval), va="bottom", ha="center"
    #     )
    # plt.xlabel("城市")
    # plt.ylabel("最低价 (元/月)")
    # plt.title("各城市房价最低价对比")
    # plt.show()

    # # 绘制中位数条形图
    # plt.figure(figsize=(10, 6))
    # bars = plt.bar(categories, medians, color=colors)
    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(
    #         bar.get_x() + bar.get_width() / 2, yval, int(yval), va="bottom", ha="center"
    #     )
    # plt.xlabel("城市")
    # plt.ylabel("中位数 (元/月)")
    # plt.title("各城市房价中位数对比")
    # plt.show()

    unit_price_summaries = [
        BJ.get_unit_price_summary(),
        SH.get_unit_price_summary(),
        GZ.get_unit_price_summary(),
        SZ.get_unit_price_summary(),
        CD.get_unit_price_summary(),
    ]

    # 提取绘图所需的值
    means = [summary["单位面积价格均价"] for summary in unit_price_summaries]
    maxes = [summary["单位面积价格最高价"] for summary in unit_price_summaries]
    mins = [summary["单位面积价格最低价"] for summary in unit_price_summaries]
    medians = [summary["单位面积价格中位数"] for summary in unit_price_summaries]
    categories = ["北京", "上海", "广州", "深圳", "成都"]
    colors = [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(len(categories))
    ]
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    # 绘制均价条形图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, means, color=colors)
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            va="bottom",
            ha="center",
        )
    plt.xlabel("城市")
    plt.ylabel("均价 (元/平米/月)")
    plt.title("各城市单位面积房价均价对比")
    plt.show()

    # 绘制最高价条形图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, maxes, color=colors)
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            va="bottom",
            ha="center",
        )
    plt.xlabel("城市")
    plt.ylabel("最高价 (元/平米/月)")
    plt.title("各城市单位面积房价最高价对比")
    plt.show()

    # 绘制最低价条形图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, mins, color=colors)
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            va="bottom",
            ha="center",
        )
    plt.xlabel("城市")
    plt.ylabel("最低价 (元/平米/月)")
    plt.title("各城市单位面积房价最低价对比")
    plt.show()

    # 绘制中位数条形图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, medians, color=colors)
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            va="bottom",
            ha="center",
        )
    plt.xlabel("城市")
    plt.ylabel("中位数 (元/平米/月)")
    plt.title("各城市单位面积房价中位数对比")
    plt.show()
