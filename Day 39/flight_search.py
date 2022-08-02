import requests

class FlightSearch:
    def __init__(self):
        self.kiwi_search_api_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        self.kiwi_location_api_endpoint = 'https://tequila-api.kiwi.com/locations/query'
        self.kiwi_api_key = ''
