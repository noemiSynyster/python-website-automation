import pytest
import requests


@pytest.fixture
def products_response(base_url):
    return requests.get(f"{base_url}/products")


def test_get_products_returns_200(products_response):
    assert products_response.status_code == 200


def test_get_products_returns_json_with_data_key(products_response):
    body = products_response.json()
    assert "data" in body
    assert isinstance(body["data"], list)