import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))
# print()
# print(data.cond)
#
# data_dict = data.to_dict()
# print(data_dict)
# print()

# temp_list = data["temp"].to_list()
# avg = sum(temp_list)//len(temp_list)
# print(f"average temparature = {avg}")
#
# print(data["temp"].mean())
# # print(data["temp"].max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

s_grey = data[data["Primary Fur Color"] == "Gray"]
grey = len(s_grey["Primary Fur Color"].to_list())

s_red = data[data["Primary Fur Color"] == "Cinnamon"]
red = len(s_red["Primary Fur Color"].to_list())

s_black = data[data["Primary Fur Color"] == "Black"]
black = len(s_black["Primary Fur Color"].to_list())

new_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

pandas.DataFrame(new_data).to_csv("squirrel_color.csv")



