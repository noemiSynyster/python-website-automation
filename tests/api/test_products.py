import pytest
import requests


@pytest.fixture
def products_response(base_url):
    return requests.get(f"{base_url}/products")


@pytest.fixture
def first_category_id(base_url):
    response = requests.get(f"{base_url}/categories")
    categories = response.json()
    leaf_categories = [c for c in categories if c["parent_id"] is not None]
    return leaf_categories[0]["id"]


def test_get_products_returns_200(products_response):
    assert products_response.status_code == 200


def test_get_products_returns_json_with_data_key(products_response):
    body = products_response.json()
    assert "data" in body
    assert isinstance(body["data"], list)


def test_get_products_filtered_by_category_returns_only_matching_products(base_url, first_category_id):
    response = requests.get(f"{base_url}/products", params={"by_category": first_category_id})

    assert response.status_code == 200
    products = response.json()["data"]
    assert len(products) > 0
    assert all(product["category"]["id"] == first_category_id for product in products)