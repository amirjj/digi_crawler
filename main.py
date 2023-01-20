import argparse
import glob
import os
import json
import re
import sys

from parsers import JSONParser
from requester import JSONRequester
from config import ROOT_APIS, OUTPUT_PATH, PATTERNS, OUTPUT_PATH_JSON
from storing_utils import JSONStore


def search_json_keyword(json_data, keywords=('/search/', '/product/dkp')):
    pass

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

# def start(url_key):
#     fetch_landing_page_data(url_key)
#     get_from_file()


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
    # for link in links:
    #     print(link)
    with open(OUTPUT_PATH + os.sep +
              'fetched_links_from_api.txt', "w") as f:
        for link in links:
            f.write(link + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='digi_crawler',
        description='fetch links from Digikala and crawl in them and fetch '
                    'data',
    )
    parser.add_argument(
        '--update-js-links',
        action='store_true',
        help='Pars JS files of Digikala and fetch API links for crawler stores in OUTPUT directory'
    )
    parser.add_argument(
        '--get-landing-api',
        action='store_true',
        help='GET landing page API result containing most links, APIs, promotions (store in json directory) '
    )

    parser.add_argument(
        '--update-landing-api-links',
        action='store_true',
        help='pars fetched landing API and update link database for crawler stores in OUTPUT directory'
    )

    args = parser.parse_args()
    print(args)

    if args.update_js_links:
        update_js_links()

    if args.get_landing_api:
        get_landing_api()

    if args.update_landing_api_links:
        update_landing_api_links()


# TODO: CREATE A URLBUILDER

# TODO: NEED TO BE OOP AND WRITE TEST FOR ALL

# TODO: WRITE A COHERENT APP AND SHARE ON LINKEDIN WITH A BRILLIENT TEXT
#  FINDOUT WHAT IS THE BEST WAY TO PRESENT IT IN SOCL

# TODO: JSON AND CSV OUTPUT DIR

# TODO: Write parser to nezam mohandesi

# TODO: CRAWL ON GLASSDOOR TO FIND OUT WHAT TO LEARN
