import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.shopping_cart import ShoppingCartPage
from utils.user_credentials import UserCredentials, UserCredentialForDelivery


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--headless=new" "--disable-dev-shm-usage",
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
    login_page = LoginPage(page)
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
def products_page_part_for_test(login_standart_user):
    page = login_standart_user.page
    products_page = ProductsPage(page)
    products_page.verify_opening_page()
    products_page.verify_page_loaded()
    return products_page


@pytest.fixture(scope="function")
def products_page_all_flow(login_standart_user):
    page = login_standart_user.page
    products_page = ProductsPage(page)
    products_page.verify_opening_page()
    products_page.verify_page_loaded()
    products_page.get_first_order()
    products_page.get_second_order()
    products_page.shopping_cart_backet()
    return products_page


@pytest.fixture(scope="function")
def shopping_cart_page(products_page_all_flow):
    page = products_page_all_flow.page
    shoping_cart_page = ShoppingCartPage(page)
    shoping_cart_page.verify_opening_page()
    shoping_cart_page.verify_page_loaded()
    return shoping_cart_page


@pytest.fixture(scope="function")
def checkout_information_page(shopping_cart_page):
    page = shopping_cart_page.page
    shopping_cart_page.click_checkout_button()
    checkout_information_page = CheckoutInformationPage(page)
    checkout_information_page.verify_opening_page()
    checkout_information_page.verify_page_loaded()
    return checkout_information_page


@pytest.fixture(scope="function")
def checkout_overview_page(checkout_information_page):
    page = checkout_information_page.page

    checkout_information_page.fill_first_name(UserCredentialForDelivery.STANDARD_USER_FIRST_NAME)
    checkout_information_page.fill_last_name(UserCredentialForDelivery.STANDARD_USER_LAST_NAME)
    checkout_information_page.fill_zip_code(UserCredentialForDelivery.STANDARD_USER_ZIP_CODE)
    checkout_information_page.click_continue_button()


    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.verify_opening_page()
    checkout_overview_page.verify_page_loaded()
    return checkout_overview_page



@pytest.fixture(scope="function")
def complete_page(checkout_overview_page):
    page = checkout_overview_page.page
    checkout_overview_page.click_finish_button()
    checkout_complete_page = CheckoutCompletePage(page)
    checkout_complete_page.verify_opening_page()
    checkout_complete_page.verify_page_loaded()
    return checkout_complete_page