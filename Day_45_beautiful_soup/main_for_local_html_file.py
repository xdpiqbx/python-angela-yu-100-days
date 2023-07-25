from bs4 import BeautifulSoup

website_file = './website.html'
with open(website_file, encoding="utf8") as file:
    # html_doc = file.read()
    soup = BeautifulSoup(file, 'html.parser')

# print(soup.prettify())  # Will prettify html output
print(soup.title)  # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)  # Angela's Personal Site

print(soup.p)  # get first p tag
print(soup.find_all(name="p"))  # get all p tags to list

all_anchors = soup.find_all(name="a")

for a_tag in all_anchors:
    print(a_tag.getText())
    print(a_tag.get('href'))

print(soup.find(name='h1', id='name'))

print(soup.find(name='h3', class_="heading"))

# here you can use CSS selectors
print(soup.select_one(selector="p em strong a"))

print(soup.select(".heading"))





