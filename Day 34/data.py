import requests
import random

class data:
    def __init__(self):
        pass

    def get_questions(self):
        response = requests.get(f"https://opentdb.com/api.php?amount={random.randint(0, 20)}&type=boolean")
        return response.json()["results"]
