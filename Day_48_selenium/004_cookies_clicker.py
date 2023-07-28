from time import sleep, time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver

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


def buy_available_upgrades():
    for upgrade in upgrades.find_elements(By.CSS_SELECTOR, '.enabled'):
        while 'enabled' in upgrade.get_attribute('class'):
            upgrade.click()


def buy_available_products():
    unlocked = products.find_elements(By.CSS_SELECTOR, ".unlocked.enabled")
    unlocked = unlocked[::-1]
    for product in unlocked:
        while 'enabled' in product.get_attribute('class'):
            product.click()


def click_shimmer_if_exists():
    for shimmer in shimmers.find_elements(By.CLASS_NAME, 'shimmer'):
        shimmer.click()
        print("Shimmer was clicked")


seconds_timer_stop = time() + 5
minutes_timer_stop = time() + 5000 * 60

while True:
    big_cookie.click()
    click_shimmer_if_exists()

    if seconds_timer_stop < time():
        try:
            buy_available_upgrades()
            buy_available_products()
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
        seconds_timer_stop = time() + 5

    if minutes_timer_stop < time():
        cookies_per_second = driver.find_element(By.ID, 'cookiesPerSecond')
        print("Cookies " + cookies_per_second.text)
        break
