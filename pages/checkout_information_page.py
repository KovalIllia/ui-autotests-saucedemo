from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure

from utils.user_credentials import UserCredentialForDelivery


class CheckoutInformationLocators:
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(),'Checkout: Your Information')]"
    FIRST_NAME_FIELD="//input[@class='input_error form_input' and @placeholder='First Name']"
    LAST_NAME_FIELD= "//input[@class='input_error form_input' and @placeholder='Last Name']"
    ZIP_CODE="//input[@class='input_error form_input' and @placeholder='Zip/Postal Code']"
    CANCEL_BUTTON="//button[@class='btn btn_secondary back btn_medium cart_cancel_link' and @data-test='cancel']"
    CONTINUE="//input[@class='submit-button btn btn_primary cart_button btn_action' and @data-test='continue' ]"

class CheckoutInformationPage(LoginPage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.locators=CheckoutInformationLocators

    def verify_opening_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def verify_page_loaded(self):
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.LAST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.CANCEL_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.CONTINUE)).to_be_visible()

    def fill_first_name(self,firstname: str):
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_be_enabled()
        self.page.fill(self.locators.FIRST_NAME_FIELD, firstname)
        expect(self.page.locator(self.locators.FIRST_NAME_FIELD)).to_have_value(firstname)

    def fill_last_name(self):
        pass

    def fill_zip_code(self):
        pass