import pandas as p

data = p.read_csv('Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv', usecols=['Primary Fur Color'])

squirrels_by_colors = data.groupby('Primary Fur Color')['Primary Fur Color'].count()
squirrels_by_colors.rename({0: 'Fur Color', 1:'Count'})
print(squirrels_by_colors)
squirrels_csv = squirrels_by_colors.to_csv('squirrels count.csv')
print(squirrels_csv)
