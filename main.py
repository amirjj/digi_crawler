import os
import json

from parser import JSONParser
from requester import JSONRequester
from config import ROOT_APIS
from storing_utils import JSONStore


def get_json_from_file(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
        return data



def start(url_key):
    # json_requester = JSONRequester(ROOT_APIS[url_key])
    # response = json_requester.get()
    # js_store = JSONStore(response, prefix=url_key)
    # js_store.store()
    file = os.path.join(os.getcwd(), 'output', 'json', 'v1_20230115203651.json')
    json_data = get_json_from_file(file)
    parser = JSONParser(json_data)
    parser.fetch_keys()


if __name__ == "__main__":
    start('v1')






# TODO: FETCH INDEX & GET ALL CATEGORIES FIRST LIKE
#  (/search/category-protein-foods/, /search/category-groceries/)

# TODO: _next/static/chunks/

# TODO: fetch links from jsons

# TODO: CREATE A URLBUILDER

# TODO: MAKE IT INTERACTIVE COMMANDLINE APP

# TODO: NEED TO BE OOP AND WRITE TEST FOR ALL

# TODO: WRITE A COHERENT APP AND SHARE ON LINKEDIN WITH A BRILLIENT TEXT
#  FINDOUT WHAT IS THE BEST WAY TO PRESENT IT IN SOCL

# TODO: JSON AND CSV OUTPUT DIR

# TODO: Write parser to nezam mohandesi

# TODO: CRAWL ON GLASSDOOR TO FIND OUT WHAT TO LEARN


    # print(response_dict.get('data'))
    # print(response_dict['data'])

    # print(response.text)
    # soup = BeautifulSoup(response.text, 'html.parser')
    #
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.p)
    # print(soup.p['class'])
    # print(soup.a)
    # print(soup.find_all('a'))
    # soup.find('div', attrs={'class': 'content'})
    # soup.find_all('li', attrs={'class': 'list'})
    # soup.select('#id')
    # soup.select_one('#id')
    # selector = '#ProductListPagesWrapper > section.w-full.grow-1.pos-relative > div.product-list_ProductList__pagesContainer__zAhrX.product-list_ProductList__pagesContainer--withSidebar__17nz1 > div:nth-child(2) > a > div > article > div.d-flex.grow-1.pos-relative.flex-column > div.grow-1.d-flex.flex-column.ai-stretch.jc-start > div.pt-1.d-flex.flex-column.ai-stretch.jc-between > div:nth-child(1) > div > span'
    # soup.select_one(selector)
