import allure
from playwright.sync_api import Browser, Page, expect
from utils.user_credentials import UserCredentials


class LoginPageLocators:
    LOGIN_PAGE_TITTLE = "//div[@class='login_logo']"
    INPUT_FIELD_USERNAME = "//input[@class='input_error form_input' and @placeholder='Username' and @name='user-name']"
    INPUT_FIELD_PASSWORD = "//input[@class='input_error form_input' and @placeholder='Password' and @name='password']"
    LOGIN_BUTTON = "//input[@type='submit']"
    ERROR_MESSAGE="//h3[@data-test='error']"

class LoginPage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.locators = LoginPageLocators()

    @allure.step("Opening the start page (URL)")
    def open_page(self):
        self.page.goto(self.BASE_URL)

    @allure.step("Verify page loaded successfully")
    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.LOGIN_PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.INPUT_FIELD_USERNAME)).to_be_visible()
        expect(self.page.locator(self.locators.INPUT_FIELD_PASSWORD)).to_be_visible()
        expect(self.page.locator(self.locators.LOGIN_BUTTON)).to_be_visible()

    @allure.step("Verify loaded URL of loaded page")
    def verify_loaded_url(self):
        expect(self.page).to_have_url(self.BASE_URL)

    @allure.step("Verify login form elements are visible and enabled")
    def verify_form_elements_ready(self):
        expect(self.page.locator(self.locators.INPUT_FIELD_USERNAME)).to_be_empty()
        expect(self.page.locator(self.locators.INPUT_FIELD_USERNAME)).to_be_enabled()
        expect(self.page.locator(self.locators.INPUT_FIELD_PASSWORD)).to_be_empty()
        expect(self.page.locator(self.locators.INPUT_FIELD_PASSWORD)).to_be_enabled()
        expect(self.page.locator(self.locators.LOGIN_BUTTON)).to_be_enabled()


    @allure.step("input login")
    def fill_username(self, username: str):
        self.page.fill(self.locators.INPUT_FIELD_USERNAME, username)
        expect(self.page.locator(self.locators.INPUT_FIELD_USERNAME)).to_have_value(username)

    def fill_password(self, password: str):
        self.page.fill(self.locators.INPUT_FIELD_PASSWORD, password)
        expect(self.page.locator(self.locators.INPUT_FIELD_PASSWORD)).to_have_value(password)


    def click_login_button(self):
        expect(self.page.locator(self.locators.LOGIN_BUTTON)).to_be_enabled()
        self.page.click(self.locators.LOGIN_BUTTON)

    @allure.step("Verify error message for invalid credentials")
    def verify_error_message(self,expected_error:str):
        expect(self.page.locator(self.locators.ERROR_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.locators.ERROR_MESSAGE)).to_contain_text(expected_error)



