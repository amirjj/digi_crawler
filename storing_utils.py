import json
import os
import random
from datetime import datetime
from abc import ABC, abstractmethod
from config import OUTPUT_PATH_JSON


class BaseStore(ABC):
    @abstractmethod
    def store(self):
        pass


class JSONStore(BaseStore):
    def __init__(self, response, prefix=None, suffix='json'):
        self.response = response
        self.prefix = self.generate_prefix(prefix)
        self.suffix = suffix

    @staticmethod
    def generate_prefix(prefix):
        if not prefix:
            return f'unknown_{datetime.now().strftime("%Y%m%d%H%M%S")}'
        return f'{prefix}_{datetime.now().strftime("%Y%m%d%H%M%S")}'

    def store(self):
        if not os.path.exists(OUTPUT_PATH_JSON):
            os.makedirs(OUTPUT_PATH_JSON)
        filename = OUTPUT_PATH_JSON + os.sep + f'{self.prefix}.{self.suffix}'
        with open(filename, 'w') as f:
            f.write(json.dumps(self.response))


class CSVStore(BaseStore):
    pass

class DBStore(BaseStore):
    pass

