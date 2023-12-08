import pandas as pd
import matplotlib.pyplot as plt


def calculate_and_visualize_average_price(file_path):
    # 读取 CSV 文件
    data = pd.read_csv(file_path)

    # 根据板块分组并计算每个板块的平均价格
    average_prices_by_area = data.groupby("板块")["价格(元/月)"].mean().reset_index()

    # 按平均价格降序排序
    sorted_average_prices = average_prices_by_area.sort_values(
        by="价格(元/月)", ascending=False
    )

    # 可视化数据

    plt.rcParams.update({"font.size": 5})
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.figure(figsize=(18, 8))
    bars = plt.bar(
        sorted_average_prices["板块"], sorted_average_prices["价格(元/月)"], color="skyblue"
    )

    plt.xlabel("板块")
    plt.ylabel("平均价格(元/月)")
    plt.title("各板块的平均租金价格")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    return sorted_average_prices


# 指定文件路径
file_path = "data/cd.csv"  # 请替换为您的文件路径

# 计算、排序并可视化结果
sorted_average_prices = calculate_and_visualize_average_price(file_path)
# print(sorted_average_prices.head())  # 显示前几行排序后的结果
