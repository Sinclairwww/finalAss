import pandas as pd
import matplotlib.pyplot as plt


def analyze_housing_affordability(file_path, city_name):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Beijing's per capita GDP
    gdp_per_capita = 190000  # in Yuan

    # Calculating the number of square meters of housing that can be afforded for a year with the GDP
    data["affordable_area_sqm"] = gdp_per_capita / (data["单位面积价格(元/平米/月)"] * 12)

    # Removing extreme points (outliers) for a clearer view
    # Using the Interquartile Range (IQR) method to identify outliers
    Q1 = data["affordable_area_sqm"].quantile(0.25)
    Q3 = data["affordable_area_sqm"].quantile(0.75)
    IQR = Q3 - Q1

    # Defining outliers as points outside of Q1 - 1.5*IQR and Q3 + 1.5*IQR
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filtering the data to exclude outliers
    filtered_data = data[
        (data["affordable_area_sqm"] >= lower_bound)
        & (data["affordable_area_sqm"] <= upper_bound)
    ]

    # Creating a histogram to show the distribution of affordable housing area
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(10, 6))
    plt.hist(
        filtered_data["affordable_area_sqm"],
        bins=30,
        color="skyblue",
        edgecolor="black",
    )

    # Adding value labels to each bar
    for rect in plt.gca().patches:
        height = rect.get_height()
        plt.gca().text(
            rect.get_x() + rect.get_width() / 2,
            height + 5,
            f"{int(height)}",
            ha="center",
            va="bottom",
        )

    plt.title(f"{city_name}GDP可租住面积分布图")
    plt.xlabel("面积(平方米)")
    plt.ylabel("频数")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # analyze_housing_affordability("data/bj.csv", "北京")
    analyze_housing_affordability("data/sh.csv", "上海")
    analyze_housing_affordability("data/gz.csv", "广州")
    analyze_housing_affordability("data/sz.csv", "深圳")
    analyze_housing_affordability("data/cd.csv", "成都")
