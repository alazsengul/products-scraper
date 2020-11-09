from selectorlib import Extractor
from selectorlib.formatter import Formatter
import requests
import json
import time

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

    request = requests.get(url, headers = headers)

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
# Amazon Image Formatter
# -> returns highest quality image from Amazon's various sizes
#
# text: (STRING) comma-separated image urls
#

class AmazonImage(Formatter):
    def format(self, text):
        return text.split(", ")[-1].split()[0]

# ------------------------------------------------------------------------------
# CONSTRUCT AMAZON URL
# -> returns constructed Amazon URL
#
# search_query: (STRING) user's raw search query
# page_number: (INT) search result page number
# time_stamp: (INT) current Unix time stamp
# 

def construct_amazon_url(search_query, page_number, time_stamp=int(time.time())):
    
    base_url = "https://www.amazon.com/s?"
    query_param = "k=" + "+".join(search_query.split())
    page_param = "page=" + str(page_number)
    dt_param = "qid=" + str(time_stamp)
    
    if page_number == 1:
        ref_param = "ref=nb_sb_noss"
        return base_url + "&".join([query_param, dt_param, ref_param])
    else:
        ref_param = "ref=sr_pg_" + str(page_number)
        return base_url + "&".join([query_param, page_param, dt_param, ref_param])

# ------------------------------------------------------------------------------
# SCRAPE AMAZON
# -> returns Amazon search results
#
# search_query: (STRING) user's raw search query
# page_last: (INT) last product page number in range to scrape
# page_first: (INT) first product page number in range to scrape
# time_delay: (INT) amount of time to pause for before each page request
#

def scrape_amazon(search_query, page_last, page_first=1, time_delay=2):

    formatters = Formatter.get_all()
    amazon_extractor = Extractor.from_yaml_file("selectors/amazon.yml", formatters=formatters)

    result = []

    for page_index in range(page_first, page_last + 1):

        url_query = construct_amazon_url("weighted blanket", page_index)
        amazon_request = request_url(url_query)
        scraped_data = extract_data(amazon_extractor, amazon_request)

        result += scraped_data["products"]

    return result

if __name__ == '__main__':
    result = scrape_amazon("weighted blanket", 3)
    print(len(result))
    print(result)
