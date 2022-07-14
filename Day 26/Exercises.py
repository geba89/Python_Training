# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆

# #Write your 1 line code 👇 below:

# squared_numbers = [num * num for num in numbers]

# #Write your code 👆 above:

# print(squared_numbers)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:

# result = [num for num in numbers if num % 2 == 0]

# #Write your code 👆 above:

# print(result)

# file1 = open('Day 26/file1.txt')
# file2 = open('Day 26/file2.txt')

# numbers1 = file1.readlines()
# numbers2 = file2.readlines()

# result = [int(num) for num in numbers1 if num in numbers2]

# # Write your code above 👆

# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
words = sentence.split()
# Write your code below:

result = [f"{word} : {len(word)}" for word in words]

print(result)




