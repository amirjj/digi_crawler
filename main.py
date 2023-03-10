import argparse
import functions


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
    parser.add_argument(
        '--crawl-trough-urls',
        action='store_true',
        help='Start crawling in Digikala URLs already fetched'
    )
    parser.add_argument(
        '--crawl-product-pages',
        action='store_true',
        help='Crawl trough all final pages'
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

    if args.crawl_trough_urls:
        functions.crawl_trough_urls()

    if args.crawl_product_pages:
        functions.crawl_product_pages()


# TODO: NEED TO BE OOP AND WRITE TEST FOR ALL

# TODO: WRITE A COHERENT APP AND SHARE ON LINKEDIN WITH A BRILLIENT TEXT
#  FINDOUT WHAT IS THE BEST WAY TO PRESENT IT IN SOCL

# TODO: Write parser to nezam mohandesi
