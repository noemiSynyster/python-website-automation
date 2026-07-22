import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

API_BASE_URL = "https://api.practicesoftwaretesting.com"
UI_BASE_URL = os.getenv("BASE_URL", "https://practicesoftwaretesting.com")


@pytest.fixture
def base_url():
    return API_BASE_URL


@pytest.fixture
def ui_base_url():
    return UI_BASE_URL


@pytest.fixture
def test_user_credentials():
    return {
        "email": os.getenv("TEST_USER_EMAIL"),
        "password": os.getenv("TEST_USER_PASSWORD"),
    }


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser

    browser.quit()