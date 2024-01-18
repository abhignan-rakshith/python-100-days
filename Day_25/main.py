# with open(file="weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# Learnt how to use the csv.reader(csv file_obj) method from csv module
# But it's very tedious to work with...so we instead use the pandas library

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data['temp'].to_list()
#print(temp_list)

# sum_list = sum(temp_list)
# len_list = len(temp_list)
# print(sum_list/len_list)

#print(data['temp'].mean())
#print(data['temp'].max())

# Get data from columns
#print(data.condition)

# Get data from rows
#print(data[data.day == "Monday"])

# Row of data that had maximum temperature
#print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# #print(monday.condition)
# celsius = monday.temp.iloc[0]
# fahrenheit = (celsius * (9/5)) + 32
# print(fahrenheit)

# Create a DataFrame from scratch

data_dict = {
    "students": ["Amy", "James", "Michel"],
    "scores": [70, 81, 68],
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")


