import requests
from src.scraping import request_url

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
