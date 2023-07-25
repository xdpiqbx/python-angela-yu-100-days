from bs4 import BeautifulSoup
import requests

temp_html = "./resources/movies-html.html"
result_txt = "./resources/result_movies.txt"

# Save Html page to file .html
# url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# response = requests.get(url=url)
# with open(temp_html, "w", encoding="utf8") as file:
#     file.write(response.text)

# Open Html file to soup
with open(temp_html, encoding="utf8") as file:
    soup = BeautifulSoup(file, 'html.parser')

titles = soup.select('div.article-title-description__text h3.title')

titles_texts = [title.getText() for title in titles]
clear_titles = list()
for title in titles_texts:
    parted = title.split(' ')
    parted.pop(0)
    clear_titles.append(" ".join(parted))

clear_titles = clear_titles[::-1]

final_string = ''
for i, title in enumerate(clear_titles, start=1):
    final_string += f"{i}) {title}\n"


with open(result_txt, "w", encoding="utf8") as file:
    file.write(final_string)
