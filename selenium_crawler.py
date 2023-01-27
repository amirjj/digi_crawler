import os

from selenium import webdriver
from time import sleep
from config import PRODUCT_DKP_PATH


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
        os.makedirs(path)
        return path

    def pars_each_link(self, link):
        self.driver.get(link)
        path = self.create_dir(link)
        sleep(5)

    def start(self):
        for link in self.links:
            print(link)
            self.pars_each_link(link)

    def stop(self):
        self.driver.close()

