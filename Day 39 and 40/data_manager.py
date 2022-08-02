import requests
import os

class DataManager:
    def __init__(self):
        self.sheety_api_endpoint = 'https://api.sheety.co/7c9cb8f1c70d07d431d7ce92a7f6223a/flightDeals/prices'
        self.sheety_api_key = {"Authorization":f"Bearer {os.environ.get('SHEETY_TOKEN')}"}

    def get_data(self):
        response = requests.get(self.sheety_api_endpoint, headers=self.sheety_api_key)
        return response.json()['prices']

    def update_item(self, id, price, city, code):
        endpoint = f"{self.sheety_api_endpoint}/{id}"
        body = {'price':{
            'city':city,
            'iataCode':code,
            'lowestPrice':price
        }}

        response = requests.put(endpoint, json=body, headers=self.sheety_api_key)
