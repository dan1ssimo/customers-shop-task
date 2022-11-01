import requests


def test_products_page_is_available():
    response = requests.get("http://localhost:8895/products")
    assert response.ok
