import json
from pathlib import Path
from time import sleep, time
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (StaleElementReferenceException,
                                        ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        WebDriverException)

url = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome()
driver.get(url)

sleep(3)  # wait while the page opening

lang_eng = driver.find_element(By.ID, 'langSelect-EN')
lang_eng.click()

sleep(3)  # wait while the game opening

big_cookie = driver.find_element(By.ID, 'bigCookie')
upgrades = driver.find_element(By.ID, "upgrades")
products = driver.find_element(By.ID, 'products')
shimmers = driver.find_element(By.ID, 'shimmers')


def turn_off_volume():
    print("You have 10 seconds to turn off volume if you want =)")
    sleep(10)


def buy_available_upgrades():
    for upgrade in upgrades.find_elements(By.CSS_SELECTOR, '.enabled'):
        while 'enabled' in upgrade.get_attribute('class'):
            upgrade.click()
            sleep(0.1)


def buy_available_products():
    unlocked = products.find_elements(By.CSS_SELECTOR, ".unlocked.enabled")
    unlocked = unlocked[::-1]
    for product in unlocked:
        while 'enabled' in product.get_attribute('class'):
            product.click()
            sleep(0.1)


def click_shimmer_if_exists():
    for shimmer in shimmers.find_elements(By.CLASS_NAME, 'shimmer'):
        shimmer.click()
        print("Shimmer was clicked")
        sleep(0.5)


def save_game():
    driver.find_element(By.CSS_SELECTOR, "#prefsButton div.subButton").click()  # Open menu Options
    sleep(0.1)
    driver.find_element(By.LINK_TEXT, "Export save").click()  # Open Export save
    sleep(0.1)
    save_code = driver.find_element(By.ID, "textareaPrompt").text  # Copy save code
    sleep(0.1)
    driver.find_element(By.ID, "promptOption0").click()  # Close Export save
    sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#menu div.menuClose").click()  # Close Options
    sleep(0.1)

    data_to_file = {
        "save_date": dt.now().strftime("%d.%m.%Y %H:%M:%S"),
        "save_code": save_code
    }

    with open(Path('./save.json'), 'w', encoding='utf-8') as json_file:
        json.dump(data_to_file, json_file, indent=4)

    print("\nGame was saved")
    print(data_to_file)
    print("\n")


def load_game():
    with open(Path('./save.json'), encoding='utf-8') as json_file:
        save_code = json.loads(json_file.read()).get("save_code")
    driver.find_element(By.CSS_SELECTOR, "#prefsButton div.subButton").click()  # Open menu Options
    sleep(0.1)
    driver.find_element(By.LINK_TEXT, "Import save").click()  # Open Export save
    sleep(0.1)
    driver.find_element(By.ID, "textareaPrompt").send_keys(save_code)  # Paste code
    sleep(0.1)
    driver.find_element(By.ID, "promptOption0").click()  # Load
    sleep(0.1)
    driver.find_element(By.CSS_SELECTOR, "#menu div.menuClose").click()  # Close Options
    sleep(0.1)


seconds_timer_stop = time() + 5
minutes_timer_stop = time() + 5 * 60

turn_off_volume()

load_game()

driver.find_element(By.ID, "storeBulk10").click()

while True:
    try:
        big_cookie.click()
        click_shimmer_if_exists()

        if seconds_timer_stop < time():
            try:
                buy_available_upgrades()
                buy_available_products()
            except (StaleElementReferenceException,
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                    WebDriverException) as error:
                print(str(error))
            seconds_timer_stop = time() + 5

    except (ElementClickInterceptedException,
            ElementNotInteractableException,
            WebDriverException) as error:
        print(str(error))

    if minutes_timer_stop < time():
        save_game()
        minutes_timer_stop = time() + 5 * 60
