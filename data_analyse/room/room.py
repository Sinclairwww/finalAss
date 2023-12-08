import pandas as pd
import matplotlib.pyplot as plt


class Room:
    def __init__(self, path):
        self.data = pd.read_csv(path)
        self.grouped_data_cleaned = None
        self.clean_data()
        self.group_data()

    def clean_data(self):
        # Cleaning the data
        self.data.dropna(subset=["房型"], inplace=True)
        self.data["室的数量"] = self.data["房型"].str.extract(r"(\d+)室")
        # Remove rows where room number extraction failed
        self.data.dropna(subset=["室的数量"], inplace=True)
        self.data["室的数量"] = self.data["室的数量"].astype(int)
        # Filtering for 1, 2, and 3 rooms only
        self.data = self.data[self.data["室的数量"].isin([1, 2, 3])]

    def group_data(self):
        # Grouping the data and calculating statistics
        grouped_data_cleaned = self.data.groupby("室的数量")["价格(元/月)"].agg(
            ["mean", "max", "min", "median"]
        )
        grouped_data_cleaned.columns = ["平均价格", "最高价格", "最低价格", "中位数"]
        grouped_data_cleaned.reset_index(inplace=True)
        self.grouped_data_cleaned = grouped_data_cleaned


# Room class as defined previously


def plot_grouped_comparison_for_room(rooms, room_number, title):
    # Setting the positions and width for the bars
    pos = list(range(len(rooms)))
    width = 0.2

    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(15, 8))
    labels = ["北京", "上海", "深圳", "广州", "成都"]

    # Creating bars for each metric
    for i, metric in enumerate(["平均价格", "最高价格", "最低价格", "中位数"]):
        values = [
            room.grouped_data_cleaned[room.grouped_data_cleaned["室的数量"] == room_number][
                metric
            ].mean()
            for room in rooms
        ]
        bars = ax.bar([p + width * i for p in pos], values, width, label=metric)

        # Adding the data labels on top of the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                round(yval, 2),
                va="bottom",
                ha="center",
                fontsize=8,
            )

    # Setting the x-axis labels, title, legend, and adjusting layout
    ax.set_xticks([p + 1.5 * width for p in pos])
    ax.set_xticklabels(labels)
    ax.set_title(f"{title}（{room_number}室）")
    ax.legend(loc="upper left")
    plt.ylabel("价格 (元)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    BJ = Room("data/BJ.csv")
    SH = Room("data/SH.csv")
    SZ = Room("data/SZ.csv")
    GZ = Room("data/GZ.csv")
    CD = Room("data/CD.csv")

    # List of Room objects
    rooms = [BJ, SH, SZ, GZ, CD]

    # Plotting grouped comparison for each room type
    for room_number in [1, 2, 3]:
        plot_grouped_comparison_for_room(rooms, room_number, "城市房屋价格统计对比")
