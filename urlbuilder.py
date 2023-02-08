from config import OUTPUT_PATH, PAGES_TO_SEARCH, PRODUCT_DKP_PATH
import os


class URLBuilder:
    def __init__(self):
        self.links = self.generate_digi_urls()

    @staticmethod
    def create_url_list():
        urls = list()
        urls.append(os.path.join(OUTPUT_PATH, 'fetched_links_from_js.txt'))
        urls.append(os.path.join(OUTPUT_PATH, 'fetched_links_from_api.txt'))
        return urls

    def generate_digi_urls(self):
        urls = URLBuilder.create_url_list()
        links = set()
        for url in urls:
            with open(url, 'r') as fp:
                for line in fp:
                    links.add('https://digikala.com'+line.strip())
        return links

    def generate_product_urls(self):
        product_urls_file = list()
        for directory in PAGES_TO_SEARCH:
            path = os.path.join(PRODUCT_DKP_PATH, directory, 'urls.txt')
            product_urls_file.append(path)

        links = set()
        for url in product_urls_file:
            with open(url, 'r') as fp:
                for line in fp:
                    links.add(line)
        return links

