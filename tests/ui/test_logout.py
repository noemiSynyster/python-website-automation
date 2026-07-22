from src.ui.pages.login_page import LoginPage
from src.ui.pages.account_page import AccountPage


def test_logout_from_active_session_redirects_to_login(driver, ui_base_url, test_user_credentials):
    login_page = LoginPage(driver, ui_base_url)
    login_page.load()
    login_page.login(
        test_user_credentials["email"],
        test_user_credentials["password"],
    )
    login_page.wait_for_redirect_to_account()

    account_page = AccountPage(driver, ui_base_url)
    account_page.logout()
    account_page.wait_for_redirect_to_login()

    assert "/auth/login" in driver.current_url