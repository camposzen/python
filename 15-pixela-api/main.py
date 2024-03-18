from datetime import datetime

import requests

USERNAME = "camposzen"
TOKEN = "ahiakfhafhawfhoif"

headers = {
   "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# yesterday = datetime.now().replace(day=1)
# graph_data1 = {
#     "date": yesterday.strftime("%Y%m%d"),
#     "quantity": "2.0"
# }
# print(yesterday)
# print(today)

create_endpoint = f"{graph_endpoint}/{graph_config['id']}"
# response = requests.post(url=graph_data_endpoint, json=graph_data1, headers=headers)
# print(response.text)

graph_data2 = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many hours have you studied today? ")
}
response = requests.post(url=create_endpoint, json=graph_data2, headers=headers)
print(response.text)

# update_endpoint = f"{create_endpoint}/{graph_data2['date']}"
# graph_data3 = {
#     "quantity": "3.0"
# }
# response = requests.put(url=update_endpoint, json=graph_data3, headers=headers)
# print(update_endpoint)
# print(response.text)

# delete_endpoint = f"{create_endpoint}/{graph_data2['date']}"
# response = requests.delete(url=update_endpoint, headers=headers)
# print(delete_endpoint)
# print(response.text)
