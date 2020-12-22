# Products Scraper

![GitHub](https://img.shields.io/github/license/alazsengul/products-scraper)
![GitHub Last Commit](https://img.shields.io/github/last-commit/alazsengul/products-scraper)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alazsengul/products-scraper/python-app)
[![Codecov](https://img.shields.io/codecov/c/github/alazsengul/products-scraper)](https://codecov.io/gh/alazsengul/products-scraper/)
[![Docs](https://img.shields.io/readthedocs/products-scraper)](https://products-scraper.readthedocs.io/en/latest/)

Products Scraper is a Python API that scrapes products across a variety of sites.

### Use
Merchants may want characteristic data of existing products being sold online — such as price, variation, etc. Instead of this process being manual, this API will provide a layer of abstraction to consolidate that information.

## Installation

```bash
$ git clone https://github.com/alazsengul/products-scraper.git
$ cd products-scraper
```

## Getting Started

Import the relevant functions from the source directory.

```python
 >>> from src.scraping import scrape_amazon
 >>> scrape_amazon("weighted blankets", 3) # returns list of products (JSON)
 [...]
 >>> len(scrape_amazon("weighted blankets", 3)) # 60 Amazon products per page, 3 pages scraped
 180
 >>> scrape_amazon("weighted blankets", 3) # can result in RobotError
 RobotError: Amazon thought you were a robot, try a different request header.
```
