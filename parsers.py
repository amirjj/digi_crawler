import os
from abc import ABC, abstractmethod
from config import PATTERNS, OUTPUT_PATH, SEARCH_TREE
import re
import json


class BaseParser(ABC):

    @abstractmethod
    def parse(self):
        pass


class JSONParser(BaseParser):
    def __init__(self, json_data):
        self.json_data = json_data

    def fetch_keys(self):
        """return a complex json key hierarchy"""
        print(self.json_data)

    def parse(self):
        pass

    @staticmethod
    def search_text_for_pattern(text):
        all_patterns = "|".join(PATTERNS)
        links = re.findall(all_patterns, text)
        return links


    @staticmethod
    def search_in_js_file(file):
        with open(file, 'r') as f:
            content = f.read()

        all_patterns = "|".join(PATTERNS)
        links = re.findall(all_patterns, content)
        return links


    @staticmethod
    def recursive_fetch_keys(content):
        """
        param content: a dictionary
        :return: recursively fetch all links match PATTERNS save to class variable (return None)
        """

        if type(content) is dict:
            for key, val in content.items():
                if type(val) is str:
                    links = JSONParser.search_text_for_pattern(val)
                    if len(links) > 0:
                        JSONParser.links_list.extend(links)
                        # print(links)
                if type(val) is dict:
                    JSONParser.recursive_fetch_keys(val)
                if type(val) is list:
                    for el in val:
                        if type(el) is dict:
                            JSONParser.recursive_fetch_keys(el)
                        if type(el) is str:
                            links = JSONParser.search_text_for_pattern(el)
                            if len(links) > 0:
                                JSONParser.links_list.extend(links)
                                # print(links)

    @staticmethod
    def pars_api_for_kw(file):
        with open(file, 'r') as f:
            content = json.loads(f.read())
        # cats = content.get('data').get('main_categories').get('categories')
        JSONParser.links_list = list()
        JSONParser.recursive_fetch_keys(content)
        links = JSONParser.links_list.copy()
        JSONParser.links_list.clear()
        return links

