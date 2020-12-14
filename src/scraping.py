from selectorlib import Extractor
from selectorlib.formatter import Formatter
import requests
import json
import time

from src.selectors.amazon import AMAZON_ROBOT_MESSAGE, AMAZON_YML_STRING

class RobotError(Exception):
    pass
class ScrapingError(Exception):
    pass

def request_url(url):
    """Request a URL.

    Args:
        url (str): Website url starting with "http".

    Returns:
        Response: Response object from requesting URL.

    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(url, headers=headers)

    return response

def extract_data(extractor, response):
    """Extract relevant data from HTML.

    Args:
        extractor (Extractor): Extractor object from selectorlib and formatters.
        response (Response): Response object from requesting a URL.

    Returns:
        dict: Extracted data from HTML.

    """

    return extractor.extract(request.text)

class AmazonImage(Formatter):
    def format(self, srcset):
        """Get last image (highest quality) from Amazon's various image sizes.

        Args:
            srcset (str): Comma-separated Amazon image URLs.

        Returns:
            str: Last (highest quality) image URL from comma-separated srcset.

        """

        return srcset.split(", ")[-1].split()[0]

def construct_amazon_url(search_query, page_number, time_stamp=int(time.time())):
    """Construct an Amazon search query URL.

    Args:
        search_query (str): Raw search query.
        page_number (int): Search result page number.
        time_stamp (int): Current Unix time stamp.

    Returns:
        str: Constructed Amazon URL.

    """
    
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

# TODO: sponsored vs. not sponsored boolean
def scrape_amazon(search_query, page_last, page_first=1, pause_time=2):
    """Scrape Amazon products from a search query.

    Args:
        search_query (str): Raw search query.
        page_last (int): Last search result page to scrape.
        page_first (int, optional): First search result page to scrape. Defaults to 1.
        pause_time (int, optional): Number of seconds to pause between page scrapes. Defaults to 2.

    Returns:
        list(dict): Scraped Amazon products from search results.

    """

    formatters = Formatter.get_all()
    amazon_extractor = Extractor.from_yaml_string(AMAZON_YML_STRING, formatters=formatters)

    products = []

    for page_index in range(page_first, page_last + 1):

        url_query = construct_amazon_url(search_query, page_index)
        amazon_request = request_url(url_query)

        if AMAZON_ROBOT_MESSAGE in amazon_request.text:
            raise RobotError("Amazon thought you were a robot, try a different request header.")

        scraped_data = extract_data(amazon_extractor, amazon_request)

        if not scraped_data["products"]:
            raise ScrapingError("Amazon was not able to be scraped.")

        products += scraped_data["products"]

        if page_index < page_last:
            time.sleep(pause_time)

    return products