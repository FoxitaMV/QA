#! /usr/bin/env python
# -- coding: utf-8 --
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time
import math
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json



class TestMainPageForm():

    def __init__(self):

        with open("conf.json", "r") as f:
            conf = json.load(f)

        self.driver = webdriver.Chrome()
        driver = self.driver

        driver.get(conf['host3']) 
        assert 'Главная страница' in driver.title
        self = driver.find_element(By.ID, 'main_page_form')

        # try:
        #     self = driver.find_element(By.CSS_SELECTOR, 'div.form__section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        #     self.send_keys(Keys.ENTER)
        #     self.send_keys(Keys.ARROW_DOWN)
        #     self.send_keys(Keys.ARROW_DOWN)
        #     self.send_keys(Keys.ENTER)

        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(2)').click()
        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(1)').click()

        self = driver.find_element(By.CSS_SELECTOR, '#name').send_keys(conf['name'])
        self = driver.find_element(By.CSS_SELECTOR, '#phone').send_keys(conf['phone'])
        self = driver.find_element(By.CSS_SELECTOR, '#email').send_keys(conf['email'])

        self = driver.find_element(By.XPATH, '//*[@id="callback_form"]/div/div[3]/div[2]/div[1]/div/div/div/div[1]')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element(By.CSS_SELECTOR, '.u115-00').click()
        self = driver.find_element(By.CSS_SELECTOR, 'button.u107-00__btn > span:nth-child(1)') .click()

ts = TestMainPageForm()