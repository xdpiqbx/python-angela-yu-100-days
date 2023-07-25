from bs4 import BeautifulSoup
import requests

temp_html = "./resources/temp-html.html"

# # Save Html page to file .html
# url = "https://news.ycombinator.com/"
# response = requests.get(url=url)
# with open(temp_html, "w", encoding="utf8") as file:
#     file.write(response.text)

# Open Html file to soup
with open(temp_html, encoding="utf8") as file:
    soup = BeautifulSoup(file, 'html.parser')

a_links = soup.select('span[class=titleline] > a')
scores = soup.select('span.score')

posts = list()
for i in range(len(a_links) - 1):
    posts.append({
        'link': "https://news.ycombinator.com/" + a_links[i].get('href')
        if a_links[i].get('href').startswith('item')
        else a_links[i].get('href'),
        "title": a_links[i].getText(),
        "score": int(scores[i].getText().split(" ")[0])
    })

score = posts[0].get('score')
top_post = posts[0]
for post in posts:
    if score > post.get('score'):
        continue
    score = post.get('score')
    top_post = post

print(top_post)
