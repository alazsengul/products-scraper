# Products Scraper's documentation

---

# Introduction

> Products Scraper is a Python API for scraping data about products from online retailers.

---

# Getting Started

### Installation

Products Scraper's functions can be imported to scrape various sites.

```python
 >>> from src.scraping import scrape_amazon
 >>> scrape_amazon("weighted blankets", 3) # returns list of products (JSON)
 [...]
 >>> len(scrape_amazon("weighted blankets", 3)) # 60 Amazon products per page, 3 pages scraped
 180
 >>> scrape_amazon("weighted blankets", 3) # can result in RobotError
 RobotError: Amazon thought you were a robot, try a different request header.
```

---

```eval_rst
.. toctree::
    :maxdepth: 2
    :caption: Contents:

    modules

.. note::
    The documentation for Products Scraper is not yet complete and is currently being written.
```