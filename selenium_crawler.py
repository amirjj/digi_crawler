import os
from time import sleep
import requests
import glob


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from config import PRODUCT_DKP_PATH, PRODUCT_DKP_XPATH_PATTERN, \
    LAST_NUMBER_SELECTOR_IN_PAGINATION, COUNT_OF_PAGES_TO_NAVIGATE


class SeleniumCrawler:
    def __init__(self, links):
        self.driver = self.driver_config()
        self.links = links

    def driver_config(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        return webdriver.Chrome(chrome_options=options)

    @staticmethod
    def create_dir(link):
        dir_name = link.strip('/').split('/')[-1]
        path = os.path.join(PRODUCT_DKP_PATH, dir_name)
        if os.path.exists(path):
            return path
        os.makedirs(path)
        return path

    def save_product_urls_for_each_category(self, link_dict):
        for category_path in link_dict:
            file = os.path.join(category_path, 'urls.txt')
            with open(file, 'a+') as f:
                for link in link_dict[category_path]:
                    f.write(link+'\n')

    def pars_each_link(self, link):
        link_without_page = link
        link_page = '?page='
        page_number = 1
        last_page = 2
        product_links_to_be_save = dict()

        while page_number < last_page and page_number < COUNT_OF_PAGES_TO_NAVIGATE:
            sleep(3)
            link = link_without_page + link_page + str(page_number)
            page_number += 1
            try:
                req = requests.get(link)
            except:
                continue

            if req.status_code != 200:
                return None
            self.driver.get(link)
            category_path = self.create_dir(link_without_page)

            sleep(2)

            if last_page <= 2:
                try:
                    last_page = int(self.driver.find_element(By.CSS_SELECTOR, LAST_NUMBER_SELECTOR_IN_PAGINATION).text)
                except NoSuchElementException:
                    continue
            counter = 0
            while True:
                try:
                    counter += 1
                    product_xpath_pattern = PRODUCT_DKP_XPATH_PATTERN.format(counter=counter)
                    product_link = self.driver.find_element(By.XPATH, product_xpath_pattern)
                    # print(product_xpath_pattern)
                    href = product_link.get_attribute('href')
                    if not product_links_to_be_save.get(category_path, False):
                        product_links_to_be_save[category_path] = list()
                    if href:
                        product_links_to_be_save[category_path].append(href)
                except NoSuchElementException:
                    self.save_product_urls_for_each_category(product_links_to_be_save)
                    product_links_to_be_save.clear()
                    break
                except StaleElementReferenceException:
                    pass

    def start(self):
        for link in self.links:
            print(link)
            if link.strip('/').split('/')[-1] in os.listdir(PRODUCT_DKP_PATH):
                print("Already parsed")
                continue
            self.pars_each_link(link)
        self.stop()

    def stop(self):
        self.driver.close()

