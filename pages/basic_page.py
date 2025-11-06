import allure
from playwright.sync_api import Browser, Page, expect


class LoginPageLocators:
    LOGIN_LOGO = "div[@class='login_logo']"
    INPUT_FIELD_USERNAME = "input[@class='input_error form_input' and @placeholder='Username' and @name='user-name']"
    INPUT_FIELD_PASSWORD = "input[@class='input_error form_input' and @placeholder='Password' and @name='password']"


class LoginPage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.locators=LoginPageLocators()

    # def login(self, username: str, password: str):
    #     self.page.locator(self.locators.USERNAME).fill(username)
    #     self.page.locator(self.locators.PASSWORD).fill(password)
    #     self.page.locator(self.locators.LOGIN_BUTTON).click()
