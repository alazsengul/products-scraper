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

def test_valid_url():
    r = request_url("https://www.google.com/search?q=best+weighted+blankets&hl=en&source=lnms&tbm=shop")
    assert r.ok

def test_invalid_url():
    try:
        r = request_url("tHiS_iS_nOt_A_vAlId_UrL")
    except Exception as e:
        assert type(e).__name__ == 'MissingSchema'
    else:
        assert False
