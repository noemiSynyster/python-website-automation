# conftest.py
import pytest

BASE_URL = "https://api.practicesoftwaretesting.com"


@pytest.fixture
def base_url():
    return BASE_URL