from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, ui_base_url):
        self.driver = driver
        self.base_url = ui_base_url
        self.wait = WebDriverWait(driver, 10)

    def wait_for_cloudflare_challenge_to_clear(self):
        WebDriverWait(self.driver, 20).until_not(
            lambda d: "Just a moment" in d.title
        )