from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://www.python.org/"

driver = webdriver.Chrome()
driver.get(url)

upcoming_events = driver.find_elements(By.CSS_SELECTOR, "div.event-widget div ul.menu li")
upcoming_events_dict = dict()
for i, li_event in enumerate(upcoming_events):
    time = li_event.find_element(By.TAG_NAME, 'time')
    anchor = li_event.find_element(By.TAG_NAME, 'a')
    upcoming_events_dict[i] = {
        "time": time.text,
        "name": anchor.text,
        "link": anchor.get_attribute("href"),
    }

print(upcoming_events_dict)

# for i, li_event in enumerate(upcoming_events):
#     upcoming_events_dict[i] = {
#         "time": datetime.fromisoformat(
#             li_event.find_element(By.TAG_NAME, 'time').get_attribute("datetime")
#         ).strftime("%Y-%m-%d"),
#         "name": li_event.find_element(By.TAG_NAME, 'a').text,
#         "link": li_event.find_element(By.TAG_NAME, 'a').get_attribute("href"),
#     }

