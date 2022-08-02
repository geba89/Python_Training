#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager as dm
import flight_search as fs
import notification_manager as nm
import flight_data as fd
import datetime as dt

update_sheety_data = False
data_manager = dm.DataManager()
flight_search = fs.FlightSearch()
#flight_data = fd.FlightData()
sms_manager = nm.NotificationManager()

#check if all codes are populated, if not then update it:
sheety_data = data_manager.get_data()
for city in sheety_data:
    if not city['iataCode']:
        update_sheety_data = True
        code = flight_search.get_airport_code(city['city'])
        data_manager.update_item(city['id'], city['lowestPrice'], city['city'], code)

#if there was code missing, retrive sheety once again to update data:
if update_sheety_data:
    sheety_data = data_manager.get_data()

#check flight prices
for city in sheety_data:
    cheapest_price = city['lowestPrice']
    cheapest_link = ''
    cheapest_destination = '' 
    cheapest_departure = ''
    cheapest_arrival = ''

    flights = flight_search.get_all_flights_to_airport(city['iataCode'])
    
    for flight in flights:
        if flight['price'] < cheapest_price:
            cheapest_price = flight['price']
            cheapest_transfers = [len(flight['route'])-2]
            cheapest_destination = flight['cityTo']
            cheapest_link = flight['deep_link']
            cheapest_departure = dt.datetime.strptime(flight['route'][0]['local_departure'], "%Y-%m-%dT%H:%M:%S.000Z").strftime('%Y/%m/%d')
            cheapest_arrival = dt.datetime.strptime(flight['route'][len(flight['route'])-1]['local_departure'], "%Y-%m-%dT%H:%M:%S.000Z").strftime('%Y/%m/%d') 
    if city['lowestPrice'] > cheapest_price:
        message_body = f'We have found a cheapest flight from Warsaw to {cheapest_destination} priced: {cheapest_price}. From:{cheapest_departure} - To:{cheapest_arrival}. Transfers between: {cheapest_transfers}. Link: {cheapest_link}'
        sms_manager.send_notification(message_body)