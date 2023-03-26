import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = data["Primary Fur Color"].unique()

colors_count = []

for color in fur_colors:
    if isinstance(color, str):
        colors_count.append({
            "Fur Color": color,
            # "Count": data[data["Primary Fur Color"] == color].count()["Primary Fur Color"]
            "Count": len(data[data["Primary Fur Color"] == color])
        })

data_frame = pandas.DataFrame(colors_count)

print(data_frame.to_csv())