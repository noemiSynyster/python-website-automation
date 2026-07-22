from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.ui.pages.base_page import BasePage


class AccountPage(BasePage):
    USER_MENU_BUTTON = (By.ID, "menu")
    SIGN_OUT_LINK = (By.CSS_SELECTOR, "[data-test='nav-sign-out']")

    def logout(self):
        menu_button = self.wait.until(EC.element_to_be_clickable(self.USER_MENU_BUTTON))
        menu_button.click()

        sign_out_link = self.wait.until(EC.element_to_be_clickable(self.SIGN_OUT_LINK))
        sign_out_link.click()

    def wait_for_redirect_to_login(self):
        self.wait.until(EC.url_contains("/auth/login"))