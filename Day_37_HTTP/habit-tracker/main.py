import requests
from dotenv import dotenv_values
from datetime import datetime

env = dotenv_values("../../.env")

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = env['PIXELA_USER_NAME']
TOKEN = env['PIXELA_API_KEY']
GRAPH_ID = "graph1"

# ---------------------------------- Do it ONE time to create user ----------------------------------
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# ---------------------------------- To create graph ----------------------------------
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# -------------------------------------------------------------------------------------

# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# # # today = datetime(year=2023, month=5, day=7).strftime("%Y%m%d")
# # today = datetime.now().strftime("%Y%m%d")
# # pixel_data = {
# #     "date": today,
# #     "quantity": "12.4"
# # }
# # response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
# # print(response.text)
# # print(today)

# ------------------------------------------------------------------------------------- UPDATE (PUT)

# update_day = datetime(year=2023, month=5, day=7).strftime("%Y%m%d")
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_day}"
# pixel_data = {
#     "quantity": "11.4"
# }
# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

# ------------------------------------------------------------------------------------- DELETE

delete_day = datetime(year=2023, month=5, day=7).strftime("%Y%m%d")
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_day}"
response = requests.delete(url=pixel_delete_endpoint, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
# # https://pixe.la/v1/users/xdpiqbx/graphs/graph1.html
# # https://pixe.la/v1/users/vxdpiqbxv/graphs/graph1.html
# print(graph_endpoint)
