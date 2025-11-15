from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure

from utils.user_credentials import UserCredentialForDelivery


class CheckoutInformationLocators:
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(),'Checkout: Your Information')]"
    FIRST_NAME_FIELD = (
        "//input[@class='input_error form_input' and @placeholder='First Name']"
    )
    LAST_NAME_FIELD = (
        "//input[@class='input_error form_input' and @placeholder='Last Name']"
    )
    ZIP_CODE = (
        "//input[@class='input_error form_input' and @placeholder='Zip/Postal Code']"
    )
    CANCEL_BUTTON = "//button[@class='btn btn_secondary back btn_medium cart_cancel_link' and @data-test='cancel']"
    CONTINUE_BUTTON = "//input[@class='submit-button btn btn_primary cart_button btn_action' and @data-test='continue' ]"


class CheckoutInformationPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CheckoutInformationLocators

    def verify_opening_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-one.html"
        )

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_empty()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_be_empty()
        expect(self.page.locator(self.locators.ZIP_CODE)).to_be_visible()
        expect(self.page.locator(self.locators.ZIP_CODE)).to_be_empty()
        expect(self.page.locator(self.locators.CANCEL_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE_BUTTON)).to_be_visible()

    def fill_first_name(self, firstname: str):
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_enabled()
        self.page.fill(self.locators.FIRST_NAME_FIELD, firstname)
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_have_value(
            firstname
        )

    def fill_last_name(self, last_name: str):
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_be_enabled()
        self.page.fill(self.locators.LAST_NAME_FIELD, last_name)
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_have_value(
            last_name
        )

    def fill_zip_code(self, zip_code: str):
        expect(self.page.locator(self.locators.ZIP_CODE)).to_be_visible()
        expect(self.page.locator(self.locators.ZIP_CODE)).to_be_enabled()
        self.page.fill(self.locators.ZIP_CODE, zip_code)
        expect(self.page.locator(self.locators.ZIP_CODE)).to_have_value(zip_code)

    def click_continue_button(self):
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).not_to_be_empty()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).not_to_be_empty()
        expect(self.page.locator(self.locators.ZIP_CODE)).not_to_be_empty()
        expect(self.page.locator(self.locators.CONTINUE_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE_BUTTON)).to_be_enabled()
        self.page.click(self.locators.CONTINUE_BUTTON)
