from matplotlib import use
import pandas as p

data_frame = p.read_csv('Day 26/nato_phonetic_alphabet.csv')

nato = {}
for (index, row) in data_frame.iterrows():
    nato[row.letter] = row.code

user_text = input("Enter word: ")
output_list = [nato[letters.upper()] for letters in user_text]

print(output_list)