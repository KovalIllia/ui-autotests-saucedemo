import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.user_credentials import UserCredentials


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--headless=new"
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-software-rasterizer",
                "--window-size=1920,1080",
            ],
        )
        context: BrowserContext = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        page: Page = context.new_page()
        page.set_default_timeout(4000)
        page.set_default_navigation_timeout(4000)
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def login_standart_user(page):
    login_page=LoginPage(page)
    login_page.open_page()
    login_page.verify_page_loaded()
    login_page.verify_loaded_url()
    login_page.fill_username(UserCredentials.STANDARD_USER)
    login_page.fill_password(UserCredentials.PASSWORD)
    login_page.click_login_button()
    return login_page


@pytest.fixture(scope="function")
def login_problem_user(page):
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.verify_page_loaded()
    login_page.verify_loaded_url()
    login_page.fill_username(UserCredentials.PROBLEM_USER)
    login_page.fill_password(UserCredentials.PASSWORD)
    login_page.click_login_button()
    return login_page

@pytest.fixture(scope="function")
def login_locked_user(page):
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.verify_page_loaded()
    login_page.verify_loaded_url()
    login_page.fill_username(UserCredentials.LOCKED_OUT_USER)
    login_page.fill_password(UserCredentials.PASSWORD)
    login_page.click_login_button()
    return login_page


@pytest.fixture(scope="function")
def login_visual_user(page):
    login_page = LoginPage(page)
    login_page.open_page()
    login_page.verify_page_loaded()
    login_page.verify_loaded_url()
    login_page.fill_username(UserCredentials.VISUAL_USER)
    login_page.fill_password(UserCredentials.PASSWORD)
    login_page.click_login_button()
    return login_page


@pytest.fixture(scope="function")
def products_page(login_standart_user):
    page=login_standart_user.page
    products_page = ProductsPage(page)
    products_page.verify_opening_page()
    products_page.verify_page_loaded()
    # products_page.get_first_order()
    # products_page.get_second_order()
    # products_page.shopping_cart_backet()
    return products_page