import requests
from dotenv import dotenv_values

env = dotenv_values("../../.env")

pixela_endpoint = "https://pixe.la/v1/users"
username = env['PIXELA_USER_NAME']
TOKEN = env['PIXELA_API_KEY']

# ---------------------------------- Do it ONE time to create user ----------------------------------
# user_params = {
#     "token": TOKEN,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# https://pixe.la/v1/users/xdpiqbx/graphs/graph1.html
print(graph_endpoint)
