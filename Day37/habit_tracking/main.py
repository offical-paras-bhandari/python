import requests
from datetime import datetime #from daterime module import datetime class

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "enter your user name"
TOKEN = "enter any token"
GRAPGH_ID = "enter any graph id"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url= pixela_endpoint , json = user_params)
print(response.text)

# First fill up data for creating a user_account and comment others for register for process


# https://pixe.la/v1/users/a-know/graphs
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id":GRAPGH_ID,
#     "name":"Cycling Graph",
#     "unit":"km",
#     "type":"float",
#     "color":"ichou"
# }
#
# headers = {
#     "X-USER-TOKEN":TOKEN
# }
# # response = requests.post(url=graph_endpoint,json = graph_config,headers=headers)
# # print(response.text)
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}"
#
# today = datetime.now()
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input("How many kilometers did you cycle today? "),
# }
# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "4.5"
# }

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)