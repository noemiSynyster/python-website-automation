from src.ui.pages.login_page import LoginPage


def test_login_with_valid_credentials_redirects_to_account_page(driver, ui_base_url, test_user_credentials):
    login_page = LoginPage(driver, ui_base_url)
    login_page.load()
    login_page.login(
        test_user_credentials["email"],
        test_user_credentials["password"],
    )

    login_page.wait_for_redirect_to_account()
    assert "/account" in driver.current_url

def test_login_with_invalid_password_shows_error_message(driver, ui_base_url, test_user_credentials):
    login_page = LoginPage(driver, ui_base_url)
    login_page.load()
    login_page.login(
        test_user_credentials["email"],
        "wrong-password-123",
    )

    error_text = login_page.get_error_message_text()
    assert error_text == "Invalid email or password"
    assert "/auth/login" in driver.current_url