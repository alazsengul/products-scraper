from src.scraping import request_url, AmazonImage, construct_amazon_url, scrape_amazon

# ------------------------------------------------------------------------------
# TESTS REQUEST URL

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

def test_amazon_image_formatter():

    amazon_image_srcset = (
        "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL320_.jpg 1x, "
        "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL480_QL65_.jpg 1.5x, "
        "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL640_QL65_.jpg 2x, "
        "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL800_QL65_.jpg 2.5x, "
        "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL960_QL65_.jpg 3x"
        )

    amazon_image_formatter = AmazonImage()
    highest_quality_image = amazon_image_formatter.format(amazon_image_srcset)
    assert highest_quality_image == "https://m.media-amazon.com/images/I/81MUz6PJsnL._AC_UL960_QL65_.jpg"

def test_construct_amazon_url():

    url_query = construct_amazon_url("weighted blanket", 3, time_stamp=1607719672)
    assert url_query == "https://www.amazon.com/s?k=weighted+blanket&page=3&qid=1607719672&ref=sr_pg_3"

def test_scrape_amazon():

    try:
        items = scrape_amazon("weighted blanket", 3)
        if len(items) != 180:
            assert False
    except Exception as e:
        assert type(e).__name__ == 'RobotError'

