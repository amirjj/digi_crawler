import argparse
import functions

from bs4 import BeautifulSoup


def beutitest():
    html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)



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

    parser.add_argument('--test', action='store_true')

    args = parser.parse_args()
    print(args)

    if args.update_js_links:
        functions.update_js_links()

    if args.get_landing_api:
        functions.get_landing_api()

    if args.update_landing_api_links:
        functions.update_landing_api_links()

    if args.test:
        print("asdf")
        beutitest()


# TODO: READ AND TEST BEUTIFULSOUP & ARGPARSE UNTIL THE HELL

# TODO: CREATE A URLBUILDER

# TODO: NEED TO BE OOP AND WRITE TEST FOR ALL

# TODO: WRITE A COHERENT APP AND SHARE ON LINKEDIN WITH A BRILLIENT TEXT
#  FINDOUT WHAT IS THE BEST WAY TO PRESENT IT IN SOCL

# TODO: JSON AND CSV OUTPUT DIR

# TODO: Write parser to nezam mohandesi

# TODO: CRAWL ON GLASSDOOR TO FIND OUT WHAT TO LEARN
