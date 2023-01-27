import json
from abc import ABC, abstractmethod
import requests


class BaseRequester(ABC):

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass


class JSONRequester(BaseRequester):
    """
    JSONRequester handles request to url and return response as json
    """
    def get(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            response.raise_for_status()
        if response.headers['content-type'] != 'application/json':
            raise ValueError('Not JSON')
        return response.json()

    @staticmethod
    def pretty_print(response=None):
        if response is None:
            return
        print(json.dumps(response, indent=4))

    def post(self):
        pass


class HTTPRequester:
    def get(self):
        response = requests.get(url=self.url)
        if response.status_code == 200:
            return response.content

    def post(self):
        pass
