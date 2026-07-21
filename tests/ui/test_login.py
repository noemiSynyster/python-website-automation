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