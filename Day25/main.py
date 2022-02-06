# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#            temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # max = data["temp"].max()
# # print(data[ data["temp"] == max])
# x = data[data["day"] == "Monday"]
# print(x)
# celsius = int(x.temp) * 3
# print(celsius)

# data_dict = {
#     "students": ["Ama", "Maria", "lori"],
#      "scores": [1, 2, 3]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("newd.csv")

data_squirells = pandas.read_csv("Squirells.csv")
#no_gray = data_squirells[data_squirells["Primary Fur Color"] == "Cinnamon"].count()
#print(no_gray)
all = data_squirells["Primary Fur Color"].unique()
dict = {}
ct = []
for color in all:
    no = data_squirells[data_squirells["Primary Fur Color"] == color ].count()
    ct.append(no["Primary Fur Color"])
print(ct)
dict["fur"] = all
dict["count"]= ct
print(dict)

x = pandas.DataFrame.from_dict(dict)
x.to_csv("s_count.csv")

