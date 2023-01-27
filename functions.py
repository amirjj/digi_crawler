import glob
import os
import json

from parsers import JSONParser
from requester import JSONRequester, HTTPRequester
from config import ROOT_APIS, OUTPUT_PATH, PATTERNS, OUTPUT_PATH_JSON
from storing_utils import JSONStore
from urlbuilder import URLBuilder
from selenium_crawler import SeleniumCrawler


def update_product_dkp_sublinks(links):
    sc = SeleniumCrawler(links)
    sc.start()


def crawl_trough_urls():
    bld = URLBuilder()
    bld.generate_digi_urls()
    update_product_dkp_sublinks(bld.links)


def get_json_from_file(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
        return data


def get_landing_api(url_key='v1'):
    json_requester = JSONRequester(ROOT_APIS[url_key])
    response = json_requester.get()
    # json_requester.pretty_print(response)
    js_store = JSONStore(response, prefix=url_key)
    js_store.store()


def get_from_file():
    file = os.path.join(os.getcwd(), 'output', 'json', 'v1_20230115203651.json')
    json_data = get_json_from_file(file)
    parser = JSONParser(json_data)
    parser.fetch_keys()


def update_js_links():
    file = os.path.join(OUTPUT_PATH, '3154-607956101b8ec160.js')
    links = JSONParser.search_in_js_file(file)
    with open(OUTPUT_PATH + os.sep +
              'fetched_links_from_js.txt', "w") as f:
        for link in links:
            f.write(link + '\n')


def update_landing_api_links():
    files = glob.glob(OUTPUT_PATH_JSON + os.sep + 'v1_*')
    latest_file = max(files, key=os.path.getctime)
    links = JSONParser.pars_api_for_kw(latest_file)

    with open(OUTPUT_PATH + os.sep +
              'fetched_links_from_api.txt', "w") as f:
        for link in links:
            f.write(link + '\n')

