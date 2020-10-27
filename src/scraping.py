from selectorlib import Extractor
from selectorlib.formatter import Formatter
import requests
import json
from time import sleep

# ------------------------------------------------------------------------------
# Amazon Image Formatter
# -> returns highest quality image from Amazon's various sizes
#
# text: (STRING) comma-separated image urls
#

class AmazonImage(Formatter):
    def format(self, text):
        return text.split(", ")[-1].split()[0]

# ------------------------------------------------------------------------------
# REQUEST URL
# -> returns requests object
#
# url: (STRING) website url starting with http...
#

def request_url(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    # headers = {
    #     'dnt': '1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-user': '?1',
    #     'sec-fetch-dest': 'document',
    #     'referer': 'https://www.amazon.com/',
    #     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # }

    request = requests.get(url, headers = headers)

    if request.status_code > 500:
        print(f"Request to page {url} failed.")
        return None

    return request

# ------------------------------------------------------------------------------
# EXTRACT DATA
# -> returns json of HTML extraction
#
# extractor: (OBJECT) selectorlib extractor object
# request: (OBJECT) requests object
#

def extract_data(extractor, request):
    return extractor.extract(request.text)

# ------------------------------------------------------------------------------
# SCRAPE AMAZON
# -> returns Amazon search results
#
# search_query: (STRING) user's cleaned search query
#

def scrape_amazon(search_query):

    url_query = "https://www.amazon.com/s?k=weighted+blanket&ref=nb_sb_noss"

    amazon_request = request_url(url_query)
    formatters = Formatter.get_all()
    amazon_extractor = Extractor.from_yaml_file("selectors/amazon.yml", formatters=formatters)
    scraped_data = extract_data(amazon_extractor, amazon_request)

    print(scraped_data)

    return scraped_data

if __name__ == '__main__':
    search_query = "weighted blanket"
    scrape_amazon(search_query)
