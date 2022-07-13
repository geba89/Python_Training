from audioop import avg
import csv
import pandas as p

# weather_data_file = open('Day 25/weather_data.csv', "r")
# weather_data = weather_data_file.readlines()
# weather_data_file.close()
# print(weather_data)

# with open('Day 25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)    
#     temps = []
#     print(data)
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temps.append(row[1])

# print(temps)

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
