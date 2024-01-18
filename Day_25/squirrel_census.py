import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240118.csv")

squirrel_data['Primary Fur Color'].value_counts(ascending=True).to_csv("fur_sort.csv")




