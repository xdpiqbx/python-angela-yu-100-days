from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format DD.MM.YYYY : ")
day, month, year = date.split('.')

url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
billboard_html = "./resources/billboard.html"

response = requests.get(url)
with open(billboard_html, "w", encoding="utf8") as file:
    file.write(response.text)

with open(billboard_html, encoding="utf8") as file:
    soup = BeautifulSoup(file, 'html.parser')


# titles = soup.select('.....')