import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------
# REQUEST URL
# -> returns requests object
#
# url: website url starting with http...
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

    r = requests.get(url, headers = headers)

    return r
