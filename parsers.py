import os
from abc import ABC, abstractmethod
from config import PATTERNS, OUTPUT_PATH
import re


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
    def search_in_js_file(file):
        with open(file, 'r') as f:
            content = f.read()

        all_patterns = "|".join(PATTERNS)
        links = re.findall(all_patterns, content)
        return links



