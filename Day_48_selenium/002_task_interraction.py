from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome()
driver.get(url)

# special_statistics = driver.find_element(By.ID, "articlecount")
# text = special_statistics.find_element(By.TAG_NAME, 'a').text
# print(text)

special_statistics_a = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(special_statistics_a.text)
special_statistics_a.click()  # click on link

# ----------------------------------------------------- Find by link text
# talk_link = driver.find_element(By.LINK_TEXT, 'Talk')
# talk_link.click()
