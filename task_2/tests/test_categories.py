import requests


def test_categories_page_is_available():
    response = requests.get("http://localhost:8895/categories")
    assert response.ok
