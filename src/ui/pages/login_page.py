from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-test='login-submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='login-error']")

    def __init__(self, driver, ui_base_url):
        self.driver = driver
        self.base_url = ui_base_url
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(f"{self.base_url}/auth/login")

    def login(self, email, password):
        email_field = self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT))
        email_field.send_keys(email)

        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.send_keys(password)

        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON)
        submit_button.click()

    def wait_for_redirect_to_account(self):
        self.wait.until(EC.url_contains("/account"))

    def get_error_message_text(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error_element.text