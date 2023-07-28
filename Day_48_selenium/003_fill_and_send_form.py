from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome()
driver.get(url)

form = driver.find_element(By.CSS_SELECTOR, "form.form-signin")

name = form.find_element(By.NAME, "fName")
last_name = form.find_element(By.NAME, "lName")
email = form.find_element(By.NAME, "email")
button_submit = form.find_element(By.CSS_SELECTOR, "button[type=submit]")

name.send_keys("john")
last_name.send_keys("smith")
email.send_keys("john.smith@gmail.com")
button_submit.send_keys(Keys.ENTER)

sleep(3)
