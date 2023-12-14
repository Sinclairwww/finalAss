import pandas as pd
import matplotlib.pyplot as plt


def analyze_housing_affordability_salary(file_path, city_name):
    # Load the CSV file
    data = pd.read_csv(file_path)
    salarys = {
        "北京": 13930,
        "上海": 13832,
        "广州": 11710,
        "深圳": 13086,
        "成都": 10039,
    }
    # Calculating the number of square meters of housing that can be afforded for a year with the average salary
    data["affordable_area_sqm"] = 0.3 * salarys[city_name] / (data["单位面积价格(元/平米/月)"])

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

    # Creating a histogram to show the distribution of affordable housing area based on average salary
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.figure(figsize=(10, 6))
    plt.hist(
        filtered_data["affordable_area_sqm"],
        bins=30,
        color="skyblue",
        edgecolor="black",
    )
    plt.title(f"{city_name}地区30%平均工资可负担的房屋面积分布")
    plt.xlabel("面积(㎡)")
    plt.ylabel("频数")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    analyze_housing_affordability_salary("data/bj.csv", "北京")
    analyze_housing_affordability_salary("data/sh.csv", "上海")
    analyze_housing_affordability_salary("data/gz.csv", "广州")
    analyze_housing_affordability_salary("data/sz.csv", "深圳")
    analyze_housing_affordability_salary("data/cd.csv", "成都")
