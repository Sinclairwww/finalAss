import matplotlib.pyplot as plt
import pandas as pd


def analyze_rent_data(file_path):
    """
    Analyzes the rent data from a CSV file.
    :param file_path: Path to the CSV file
    :return: Average unit area rent for each direction
    """
    # Load the data
    data = pd.read_csv(file_path)

    # Remove rows with missing data
    data_clean = data.dropna()

    # Keep only rows with a single direction in the orientation (朝向) column
    valid_directions = ["东", "南", "西", "北"]
    data_clean = data_clean[data_clean["朝向"].isin(valid_directions)]

    # Calculate and return the average unit area rent for each direction
    return data_clean.groupby("朝向")["单位面积价格(元/平米/月)"].mean()


# Function to plot the highest and lowest average rent directions for multiple cities
def plot_rent_directions(cities_data):
    highest_rent_directions = {}
    lowest_rent_directions = {}

    for city, data in cities_data.items():
        highest_rent_direction = data.idxmax()
        lowest_rent_direction = data.idxmin()
        highest_rent_directions[city] = (
            highest_rent_direction,
            data[highest_rent_direction],
        )
        lowest_rent_directions[city] = (
            lowest_rent_direction,
            data[lowest_rent_direction],
        )
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    # Plotting the highest average rent directions
    plt.figure(figsize=(10, 5))
    plt.title("各城市最高平均单位租金朝向")
    for city, (direction, rent) in highest_rent_directions.items():
        plt.bar(city, rent, label=f"{direction} ({rent:.2f}/㎡/month)")
    plt.ylabel("平均单位租金 (元/㎡/month)")
    plt.legend()
    plt.show()

    # Plotting the lowest average rent directions
    plt.figure(figsize=(10, 5))
    plt.title("各城市最低平均租金朝向")
    for city, (direction, rent) in lowest_rent_directions.items():
        plt.bar(city, rent, label=f"{direction} ({rent:.2f}/㎡/month)")
    plt.ylabel("平均单位租金 (元/㎡/month)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Assuming the data for each city is available in the specified paths
    BJ = analyze_rent_data("data/bj.csv")
    SH = analyze_rent_data("data/sh.csv")
    SZ = analyze_rent_data("data/sz.csv")
    GZ = analyze_rent_data("data/gz.csv")
    CD = analyze_rent_data("data/cd.csv")

    cities_data = {
        "北京": BJ,
        "上海": SH,
        "深圳": SZ,
        "广州": GZ,
        "成都": CD,
    }
    plot_rent_directions(cities_data)
