from urllib import response
import requests
from datetime import datetime

pixela_user = "gebaftw"
pixela_graph_id = "graph1"
pixela_graph_endpoint = f"https://pixe.la/v1/users/{pixela_user}/graphs"
pixela_create_user_endpoint = "https://pixe.la/v1/users/"
pixela_token_header = {"X-USER-TOKEN":"password"}
pixela_pixel_endpoint = f"https://pixe.la/v1/users/{pixela_user}/graphs/{pixela_graph_id}"
pixela_pixel_update_endpoint = f"https://pixe.la/v1/users/{pixela_user}/graphs/{pixela_graph_id}/{datetime.today().strftime('%Y%m%d')}"

# USER CREATION
# pixela_user_params = {"token":"password", "username":"gebaftw", "agreeTermsOfService":"yes", "notMinor":"yes"}
# response = requests.post(pixela_endpoint, json=pixela_user_params)
# print(response.json())

# Create Graph
# pixela_graph_params = {"id":"graph1", "name":"Learning to Code", "unit":"commit", "type":"int", "color":"shibafu"}
# response = requests.post(pixela_graph_endpoint, json=pixela_graph_params, headers=pixela_token_header)
# print(response.json())

#Post new pixel to a graph
#today_date = datetime.today().strftime('%Y%m%d')
#pixela_pixel_params = {"date": str(today_date), "quantity":"1" }
#response = requests.post(pixela_pixel_endpoint, json=pixela_pixel_params, headers=pixela_token_header)

#update pixel
# pixela_update_params = {"quantity":"10"}
# response = requests.put(pixela_pixel_update_endpoint, json=pixela_update_params, headers=pixela_token_header)

#delete pixel
response = requests.delete(pixela_pixel_update_endpoint, headers=pixela_token_header)


print(response.json())
