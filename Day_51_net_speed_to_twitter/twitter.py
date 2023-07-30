import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()

TWITTER_URL = "https://twitter.com/i/flow/signup"
LOGIN = os.environ["TWITTER_NAME"]
PASSWORD = os.environ["TWITTER_PASS"]


class Twitter:
    def __init__(self):
        self.twitter = webdriver.Chrome()
        self.twitter.get(TWITTER_URL)
        self.data = dict()

    def login_process(self):
        sleep(3)  # Wait for login page
        log_in_link = ('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                       'div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span')
        self.twitter.find_element(By.XPATH, log_in_link).click()
        sleep(1)

        username_input = ('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                          'div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.twitter.find_element(By.XPATH, username_input).send_keys(LOGIN)
        sleep(1)

        button_next = ('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                       'div/div/div[2]/div[2]/div/div/div/div[6]')
        self.twitter.find_element(By.XPATH, button_next).click()
        sleep(1)

        password_input = 'input[name=password]'
        self.twitter.find_element(By.CSS_SELECTOR, password_input).send_keys(PASSWORD)
        sleep(1)

        button_log_in = ('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                         'div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        self.twitter.find_element(By.XPATH, button_log_in).click()
        sleep(5)  # Wait for account page

    def write_tweet(self, tweet):
        text_area = "[data-testid*=tweetTextarea]"
        self.twitter.find_element(By.CSS_SELECTOR, text_area).click()
        sleep(0.5)
        input_tweet = 'div[data-contents=true] span[data-offset-key]'
        self.twitter.find_element(By.CSS_SELECTOR, input_tweet).send_keys(tweet)
        sleep(0.5)
        tweet_button = ('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/'
                        'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
        self.twitter.find_element(By.XPATH, tweet_button).click()
