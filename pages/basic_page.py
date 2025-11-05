import allure
from playwright.sync_api import Browser,Page, expect


class BasicPage:

    URL="https://www.saucedemo.com/"

    def __init__(self,page: Page):
        self.page=page
        # self.form=FormHelper(page) дописати коли буде використ вейтер

