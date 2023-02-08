import datetime
import json
import os

import requests
from time import sleep

from config import PRODUCT_TITLE_XPATH, DESCRIPTION_MORE_BUTTON_XPATH, \
    DESCRIPTION_XPATH, IMAGE_XPATH, PRODUCT_DETAIL_JSON_OUTPUT
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException


class ProductCrawler:
    def __init__(self, links):
        self.driver = self.driver_config()
        self.links = links

    def driver_config(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        return webdriver.Chrome(chrome_options=options)


    def store_to_json(self, product):
        filename = str(datetime.datetime.now()).replace(':', '_').replace('-', '_').replace('.', '_')+'.json'
        file_path = os.path.join(PRODUCT_DETAIL_JSON_OUTPUT, filename)
        with open(file_path, "w") as f:
            f.write(json.dumps(product))

    def start(self):
        for link in self.links:
            try:
                req = requests.get(link)
            except:
                continue

            if req.status_code != 200:
                continue

            try:
                self.driver.get(link)
            except WebDriverException:
                continue

            print(link)
            sleep(5)
            try:
                title = self.driver.find_element(By.XPATH, PRODUCT_TITLE_XPATH).text
                description = self.driver.find_element(By.XPATH, DESCRIPTION_XPATH).text
                product = dict(title=title, description=description)
                self.store_to_json(product)
                product.clear()
            except NoSuchElementException:
                "NoSuchElementException"
                continue
