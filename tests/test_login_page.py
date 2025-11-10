from pages.login_page import LoginPage
from utils.user_credentials import UserCredentials


def test_login_user(page):
    username = UserCredentials.STANDARD_USER
    password = UserCredentials.PASSWORD

    login_page = LoginPage(page)
    login_page.open_page()
    login_page.verify_page_loaded()
    login_page.verify_loaded_url()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.click_login_button()
