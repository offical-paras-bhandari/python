# data = []
# with open("226 weather-data.csv") as weather_data:
#     data = weather_data.readlines()

# import csv
#
# with open("226 weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     value = 0
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append((row[1]))
#             print(temperatures)

import pandas

# DataFrame - collection of data 2 - dimension row and column eg: csv etc
# data = pandas.read_csv("226 weather-data.csv")
# data_dict = data.to_dict()

# Series - columns
# temp = data["temp"].to_list()
# temp = data["temp"]
# print(temp.mean())
# print(temp.max())

# get data in Column
# print(data["condition"])
# print(data.condition)


# get data in row
# 1st data is dataframe 2nd selection column condition day having Monday
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# checking condition for monday
# monday = data[data.temp == data.temp.max()]
# print(monday.condition)
# print((monday.temp * 9/5)+32)


# data_dict = {
#     "student": ["shiva", "param", "vishnu"],
#     "age": [76, 56, 65]
# }
# converting dict to dataframe and convert dataframe into csv
# data = pandas.DataFrame(data_dict)
# print(data.to_csv("new_data.csv"))

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "black"])


data_dict_squirrel = {
    "fur Color": ["grey", "red", "black"],
    "count":[grey_color_count,red_color_count,black_color_count]
}
df = pandas.DataFrame(data_dict_squirrel)
df.to_csv("data_dict_squirrel.csv")


