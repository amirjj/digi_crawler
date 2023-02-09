### Crawling Digikala extracting data useful for content marketing

#### Data this crawler provides:
1. List of all product categories and brands. you can access every content list with it: 
   * `output/fetched_links_from_api.txt` and `output/fetched_links_from_js.txt` already contain sub-links to category list.
     * for example `/search/category-tablet/` is the sub-adress of all tablets like: `https://www.digikala.com/search/category-tablet/`
2. All product links fetched by crawling all categories
   * `output/product-dkp/*` contain urls already fetched, categorised based on Digikala data categorization
     * for example `output/product-dkp/category-bicycles/urls.txt` include links to all bicycles exist in Digikala
3. Product details saved as JSON file including product name, description and ...
   * for example `output/json/product_detail/*` containing json files with `{title: "some title", description: "some description.."}`


*Note: as the output stored as JSON files including realistic categories it can be easily be used to import to any database*


------
#### How to use this crawler to fetch new and updated content from Digikala:

##### Installation:
```shell
$ python -m pip install pipenv
$ pipenv install
$ pipenv shell
$ pipenv install -r requirements.txt 
```

##### Usage:

Run Help for a brief usage guidline:
```shell
$ python main.py -h
```
output:
```shell
usage: digi_crawler [-h] [--update-js-links] [--get-landing-api] [--update-landing-api-links] [--crawl-trough-urls] [--crawl-product-pages] [--test]

fetch links from Digikala and crawl in them and fetch data

options:
  -h, --help            show this help message and exit
  --update-js-links     Pars JS files of Digikala and fetch API links for crawler stores in OUTPUT directory
  --get-landing-api     GET landing page API result containing most links, APIs, promotions (store in json directory)
  --update-landing-api-links
                        pars fetched landing API and update link database for crawler stores in OUTPUT directory
  --crawl-trough-urls   Start crawling in Digikala URLs already fetched
  --crawl-product-pages
                        Crawl trough all final pages
```
The mechanism is to:
1. Fetch all categories and links from `init` API (this is the main Digikala API providing the base information like all links and categories in landing page menu)
2. Pars JS files loaded in first landing page to fetch all links and categories from them
3. generate all categories links from data gathered from 1st and 2nd stages. (eg: link to the page containing all mobiles, bicycles, TVs and ...)
4. crawl through all links fetch from stage 3 and store product details in JSON file (eg: title and description of literally all products Digikala have)
5. after all these stages finished you have all product information exist for any single product Digikala have (all these stages may take very long time but you can see a reasonable part of this data in `output/`)

