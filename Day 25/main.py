import csv
import pandas as p

data = p.read_csv('Day 25/weather_data.csv', usecols=['temp'])
print(data)
data_dict = data.to_dict()
data_list = data['temp'].to_list()

print(data_dict)
print(data_list)
avg_temp = data['temp'].mean()
print(avg_temp)
max_temp = data['temp'].max()
print(max_temp)

