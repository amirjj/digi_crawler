import os

products = ['mobile', 'perfume', 'pc']
BASE_LINK = ''

ROOT_PATH = os.getcwd()
OUTPUT_PATH_JSON = os.path.join(ROOT_PATH, 'output', 'json')
OUTPUT_PATH_CSV = os.path.join(ROOT_PATH, 'output', 'csv')


ROOT_APIS = {
    'v1': 'https://api.digikala.com/v1/',
    'v1/recommendation':
        'https://api.digikala.com/v1/recommendation/?web_page=home',

}

SEARCH_TREE = {
    'v1': {
        'data': {
            'main_categories': {
                'categories'
            }
        }
    },
    'v1/recommendation': {
        'data': {
            'categories': {

            }
        }
    },

}