#! /usr/bin/env python
# -- coding: utf-8 --
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import time
import math
import pytest
import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

d = datetime.date.fromordinal(datetime.date.today().toordinal()+1).strftime("%d/%m/%Y")
t = time.strftime("%H/%M", time.localtime())




class TestTestdriverForm():

    def __init__(self):
        with open("conf.json", "r") as f:
            conf = json.load(f)
            
        desired_cap = {
         'browserName': 'iPhone',
         'device': 'iPhone 8',
         'realMobile': 'true',
         'os_version': '11',
         'name': 'Bstack-[Python] Sample Test'
        }

        driver = webdriver.Remote(
            command_executor='https://kodix4:ufdfrtPXakc7qkbZci8Y@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
        # self.driver = webdriver.Chrome()
        # driver = self.driver
        driver.get(conf['host']) 
        assert 'Запись на тест-драйв' in driver.title
        
    
        self = driver.find_element(By.CSS_SELECTOR, '.choices')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element(By.CSS_SELECTOR, '#datepicker')
        self.send_keys(d)
        self.send_keys(Keys.ENTER)

        self = driver.find_element(By.CSS_SELECTOR, '#timepicker').send_keys(t)
        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(2)').click()
        self = driver.find_element(By.CSS_SELECTOR, 'label.u116-00:nth-child(1)').click()
        self = driver.find_element(By.CSS_SELECTOR, '#name').send_keys(conf['name'])
        self = driver.find_element(By.CSS_SELECTOR, '#phone').send_keys(conf['phone'])
        self = driver.find_element(By.CSS_SELECTOR, '#email').send_keys(conf['email'])
        self = driver.find_element(By.CSS_SELECTOR, '#processing_of_personal_data').click()
        self = driver.find_element(By.CSS_SELECTOR, 'button.u107-00__btn').click()


ts = TestTestdriverForm()