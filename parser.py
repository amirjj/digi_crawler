from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self):
        pass


class JSONParser(BaseParser):
    def __init__(self, json_data):
        self.json_data = json_data


    def fetch_keys(self):
        """return a complex json key hierarchy"""
        print(type(self.json_data))


    def parse(self):
        pass

