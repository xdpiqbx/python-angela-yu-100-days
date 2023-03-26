# import csv
import pandas

CSV_FILE = "weather_data.csv"

# with open(CSV_FILE) as weather_data:
#     data = weather_data.readlines()
#     print(data)

# with open(CSV_FILE) as weather_data:
#     csv_data = csv.reader(weather_data)
#     # print(csv_data)  # <_csv.reader object at 0x000001FF7F12ACE0>
#     temperatures = []
#     for row in csv_data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv(CSV_FILE)
# print(type(data))  # <class 'pandas.core.frame.DataFrame'> - DataFrame (2-dimensional)
# print(type(data["temp"]))  # <class 'pandas.core.series.Series'> - Series (1-dimensional)
#
# data_dict = data.to_dict()
# data_temp = data["temp"].to_dict()
#
# print(data_dict)
# print(data_temp)
#
# average_temp = data["temp"].mean()
# print(f"average_temp: {average_temp}")
#
# max_temp = data["temp"].max()
# print(f"max_temp: {max_temp}")
#
# print(data.condition)  # you can use column name as property

# print(data[data["day"] == "Monday"])
# temp_to_F = int(data[data.day == "Monday"].temp) * 9/5 + 32
# print(temp_to_F)

# Create dataframe
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65],
}

panda_data = pandas.DataFrame(data_dict)

print(panda_data.to_csv("new.csv"))
