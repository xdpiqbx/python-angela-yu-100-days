# ---------------------------------- Do it ONE time to create user ----------------------------------
# import requests
# from dotenv import dotenv_values
#
# env = dotenv_values("../../.env")
#
# pixela_endpoint = "https://pixe.la/v1/users"
#
# user_params = {
#     "token": env['PIXELA_API_KEY'],
#     "username": env['PIXELA_USER_NAME'],
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
