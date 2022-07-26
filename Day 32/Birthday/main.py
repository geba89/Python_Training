import csv
from dataclasses import replace
import datetime as dt
import smtplib
import random
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



files = ['Day 32/Birthday/letter_templates/letter_1.txt', 'Day 32/Birthday/letter_templates/letter_2.txt', 'Day 32/Birthday/letter_templates/letter_3.txt']
letters = []
csv_list = 'Day 32/Birthday/birthdays.csv'
my_email = "kotuch89@gmail.com"
my_password = "nkxgxpcxstfvkvkc"

for letter in files:
    with open(letter) as file:
        letters.append(file.readlines())

birthdays = ""

with open(csv_list) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    birthdays = []
    for row in csvreader:
        birthdays.append(row)

month = dt.datetime.now().date().month
day = dt.datetime.now().date().day

for birthdate in birthdays:
    if int(birthdate[3]) == month and int(birthdate[4]) == day:
        letter = "".join(random.choice(letters))
        letter = letter.replace("[NAME]", birthdate[0])

        with smtplib.SMTP('smtp.gmail.com', port=587) as conn:
            conn.starttls()
            conn.login(my_email, my_password)
            conn.sendmail(from_addr=my_email, to_addrs=birthdate[1], msg=f"Subject: Happy Birthday {birthdate[0]} \n\n {letter}")
    
