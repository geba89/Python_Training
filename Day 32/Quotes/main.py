import smtplib
import datetime as dt
import random


quotes = ""
email_address = "kotuch89@gmail.com"
day_of_the_week = dt.datetime.now().weekday()


if day_of_the_week == 1:
    
    with open("Day 32/Quotes/quotes.txt", "r") as file:
        quotes = file.readlines()
        file.close()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        random_quote = random.choice(quotes)
        connection.starttls()
        connection.login(user=email_address, password="")
        connection.sendmail(from_addr=email_address, to_addrs="gebskipiotr@gmail.com", msg=f"Subject: Motivation Monday! \n\n {random_quote}",)
       

