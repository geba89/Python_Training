import requests
import datetime as dt
import os

class FlightSearch:
    def __init__(self):
        self.kiwi_search_api_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        self.kiwi_location_api_endpoint = 'https://tequila-api.kiwi.com/locations/query'
        self.kiwi_api_key = os.environ.get('KIWI_KEY')

    def get_airport_code(self, airport):
        body = {'term':airport}
        header = {'apikey':self.kiwi_api_key}
        resposne = requests.get(self.kiwi_location_api_endpoint, params=body, headers=header)
        return resposne.json()['locations'][0]['code']

    def get_all_flights_to_airport(self, airport):
        today = dt.datetime.today()
        next_date = today + dt.timedelta(days=180)
        body = {'fly_from':"WAW",
                'fly_to':airport,
                'date_from':today.strftime('%d/%m/%Y'),
                'date_to':next_date.strftime('%d/%m/%Y'),
                'vehicle_type':'aircraft',
                'nights_in_dst_from':3,
                'nights_in_dst_to':7,
                'flight_type':'round'}
        header = {'apikey':self.kiwi_api_key}
        response = requests.get(self.kiwi_search_api_endpoint, params=body, headers=header)
        return response.json()['data']
        