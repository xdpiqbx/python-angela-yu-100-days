import os
from bs4 import BeautifulSoup
import requests
import json
from pathlib import Path

SAVE_TO = "./already_requested/"
data_must_be_requested = True

date = input("Which year do you want to travel to? Type the date in this format DD.MM.YYYY : ")
day, month, year = date.split('.')

# TODO: check data! if it is future change to today

FILENAME = f"{day}_{month}_{year}.json"

for filename in os.listdir(SAVE_TO):
    if filename == FILENAME:
        data_must_be_requested = False
        break

if data_must_be_requested:
    print("Data was requested")
    url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('li.o-chart-results-list__item:has(h3)')
    board = list()
    for i, song in enumerate(songs, start=1):
        board.append({
            "place": i,
            "title": song.select_one('h3').getText().strip(),
            "group": song.select_one('span').getText().strip()
        })

    with open(Path(SAVE_TO, FILENAME), 'w') as json_file:
        json.dump(board, json_file, indent=4)

with open(Path(SAVE_TO, FILENAME)) as json_file:
    hot_100 = json_file.read()

print(hot_100)
