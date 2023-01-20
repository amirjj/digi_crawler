import os

products = ['mobile', 'perfume', 'pc']
BASE_LINK = ''

ROOT_PATH = os.getcwd()
OUTPUT_PATH_JSON = os.path.join(ROOT_PATH, 'output', 'json')
OUTPUT_PATH_CSV = os.path.join(ROOT_PATH, 'output', 'csv')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'output')


ROOT_APIS = {
    'v1': 'https://api.digikala.com/v1/',
    'v1/recommendation':
        'https://api.digikala.com/v1/recommendation/?web_page=home',
}

SEARCH_TREE = {
    'data': {
        'main_categories': {
            'categories': {
                'urls': [
                        '/main/vehicles/',
                        '/main/electronic-devices/',
                        '/main/mobile/',
                        '/main/apparel/',
                        '/main/food-beverage/',
                        '/main/rural-products/',
                        '/main/mother-and-child/',
                        '/main/personal-appliance/',
                        '/main/home-and-kitchen/',
                        '/main/book-and-media/',
                        '/main/sport-entertainment/',
                ]
            }
        },
        'best_selling_products': {
            'url': '/best-selling/'
        },
        'digikala_magazine': {
            'url': '/mag/'
        },
        'digiplus': {
            'cash_back_products': {
                'url': '/search/?digiplus%5B0%5D=has_plus_cash_back'
            },
            'jet_delivery_products': {
                'url': '/search/?digiplus%5B0%5D=has_jet_delivery&sort=4'
            }
        },
        'fresh_incredible_products': {
            'url': '/fresh-offers/'
        },
        'incredible_products': {
            'url': '/incredible-offers/'
        },
        'popular_brands': {
            'urls': [
                '/brand-landing/pril/',
                '/brand-landing/persil/',
                '/brand-landing/king-star/',
                '/brand-landing/silicon-power/',
                '/brand/huawei/',
                '/brand-landing/pakshoma/',
                '/brand-landing/cheshme-noor/',
                '/brand/miscellaneous/',
                '/brand/xiaomi/',
                '/brand-landing/samsung/',
                '/brand-landing/kalleh/',
                '/brand/my/',
                '/brand/bioaqua/',
                '/brand-landing/active/',
                '/brand-landing/tsco/',
                '/brand-landing/zarmakaron/',
                '/brand-landing/leitu/',
                '/brand/shahr-glass/',
                '/brand/fresh-by-digikala/',
                '/brand/mr-rad/'
            ]
        },
        'recommendation_sub_categories': {
            'url': [
                '/search/category-mobile-phone/',
                '/search/category-cell-phone-pouch-cover/',
                '/search/category-headphone/',
                '/search/category-smart-watch/',
                '/search/category-notebook-netbook-ultrabook/',
                '/search/category-tablet/',
                '/search/category-mouse/',
                '/search/category-men-socks-tights/',
                '/search/category-station-gaming-consoles/',
                '/search/category-women-socks-/',
                '/search/category-speaker/',
                '/search/category-keyboard/',
                '/search/category-doll-house/',
                '/search/category-monitor/',
            ]
        }
    },

    'v1/recommendation': {
        'data': {
            'categories': {

            }
        }
    },
}


PATTERNS = [
    '/search/[a-zA-Z0-9-]*/',
    '/search/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',
    '/search/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/"',

    '/main/[a-zA-Z0-9-]*/',
    '/main/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',
    '/main/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',

    '/brand/[a-zA-Z0-9-]*/',
    '/brand/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',
    '/brand/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',

    '/brand-landing/[a-zA-Z0-9-]*/',
    '/brand-landing/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',
    '/brand-landing/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/[a-zA-Z0-9-]*/',

]

