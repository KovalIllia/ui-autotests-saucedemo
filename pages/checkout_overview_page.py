from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure

class CheckoutOverviewLocators:
    PAGE_TITTLE = ""
    FIRST_NAME_FIELD=""
    SECOND_NAME_FIELD=""
    CANCEL_BUTTON=""
    CONTINUE=""

class CheckoutOverviewPage(LoginPage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.locators=CheckoutOverviewLocators

    def verify_opening_page(self):
        pass

    def verify_page_loaded(self):
        pass

