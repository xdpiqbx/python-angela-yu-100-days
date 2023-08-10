import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

from zillow import Apartment

load_dotenv()

FORM_URL = f"https://forms.gle/{os.environ['GOOGLE_FORM_FOR_APARTMENTS']}"


class GoogleForm:
    def __init__(self):
        print(FORM_URL)
        self.form = webdriver.Chrome()
        self.form.get(FORM_URL)
        self.records_count = 0
        sleep(1)

    def save_all(self, apartments: iter, len_apartments):
        self.records_count = len_apartments
        self.__fill_and_send_form(next(apartments))
        next_answer_selector = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
        self.records_count -= 1
        print(f"{self.records_count} out of {len_apartments} left. {len_apartments - self.records_count} was added")
        for apartment in apartments:
            self.form.find_element(By.XPATH, next_answer_selector).click()
            sleep(1)
            self.__fill_and_send_form(apartment)
            self.records_count -= 1
            print(f"{self.records_count} out of {len_apartments} left. {len_apartments - self.records_count} was added")
        self.form.close()

    def __fill_and_send_form(self, apartment: Apartment):
        selector = "div.Xb9hP > input"
        inputs = self.form.find_elements(By.CSS_SELECTOR, selector)
        inputs[0].send_keys(apartment.address)
        inputs[1].send_keys(apartment.price)
        inputs[2].send_keys(apartment.url)
        send_selector = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
        self.form.find_element(By.XPATH, send_selector).click()
        sleep(1)
