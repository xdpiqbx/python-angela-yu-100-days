from datetime import datetime as dt
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_SPEED = 100
SPEEDTEST_URL = "https://www.speedtest.net"


class SpeedTest:
    def __init__(self):
        self.speedtest = webdriver.Chrome()
        self.speedtest.get(SPEEDTEST_URL)
        self.data = dict()

    def click_button_start(self):
        selector = ".start-button a[role=button]"
        self.speedtest.find_element(By.CSS_SELECTOR, selector).click()

    def collect_data_from_result(self):
        receiving = self.speedtest.find_element(By.CSS_SELECTOR, "[title='Receiving Time']")
        sending = self.speedtest.find_element(By.CSS_SELECTOR, "[title='Sending Time']")

        receiving_unit = receiving.find_element(By.CLASS_NAME, 'result-data-unit').text
        receiving_value = receiving.find_element(By.CLASS_NAME, 'result-data-value').text

        sending_unit = sending.find_element(By.CLASS_NAME, 'result-data-unit').text
        sending_value = sending.find_element(By.CLASS_NAME, 'result-data-value').text

        isp_title = self.speedtest.find_element(By.CSS_SELECTOR, ".js-data-isp")

        result_link_selector = ".result-data a"
        result_link = self.speedtest.find_element(By.CSS_SELECTOR, result_link_selector)

        self.data = {
            "date": dt.now().strftime("%d.%m.%Y %H:%M"),
            "isp_title": isp_title.text,
            "download": f"{receiving_value} {receiving_unit}",
            "upload": f"{sending_value} {sending_unit}",
            "result_link": result_link.get_attribute('href')
        }

    def execute(self):
        sleep(3)  # Get main page in process
        self.click_button_start()
        sleep(45)  # Measurement process
        self.collect_data_from_result()
        sleep(1)
        self.speedtest.close()

    def generate_message(self):
        return (f"My ISP \"{self.data['isp_title']}\" promise me that i will have {PROMISED_SPEED} Mbps\n"
                f"But today ({self.data['date']}) I have:\n"
                f"Download speed: {self.data['download']}\n"
                f"Upload speed: {self.data['upload']}\n"
                f"Link to results page {self.data['result_link']}\n"
                f"I think it's cool)\n"
                f"Thank you \"{self.data['isp_title']}\"")

    def get_collected_data(self):
        return self.data
