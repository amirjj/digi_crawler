import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from config import PRODUCT_DKP_PATH, PRODUCT_DKP_XPATH_PATTERN


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

    def save_product_urls_for_each_category(self, link, category_path):
        file = os.path.join(category_path, 'urls.txt')
        with open(file, 'a+') as f:
            f.write(link+'\n')

    def pars_each_link(self, link):
        self.driver.get(link)
        category_path = self.create_dir(link)
        sleep(5)
        counter = 0
        page_down = 0
        while True:
            try:
                counter += 1
                xpath_pattern = PRODUCT_DKP_XPATH_PATTERN.format(counter=counter)
                product_link = self.driver.find_element(By.XPATH, xpath_pattern)
                print(xpath_pattern)
                # product_link.send_keys(Keys.CONTROL, Keys.RETURN)
                href = product_link.get_attribute('href')
                print("current url:", self.driver.current_url)
                self.save_product_urls_for_each_category(href, category_path)
                sleep(4)
            except NoSuchElementException:
                # product_link.send_keys(Keys.PAGE_DOWN)
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                # page_down += 1
                sleep(4)






    def start(self):
        for link in self.links:
            print(link)
            self.pars_each_link(link)

    def stop(self):
        self.driver.close()

