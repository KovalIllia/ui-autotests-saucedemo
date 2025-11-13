from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


class ShoppingCartLocators:
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(), 'Your Cart')]"
    SAUCE_LABS_BACKPACK_PRODUCT = "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]"
    SAUCE_LABS_BIKE_LIGHT = "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Bike Light')]"
    CONTINUE_SHOPPING_BUTTON = "//button[@class='btn btn_secondary back btn_medium' and @name='continue-shopping']"
    CHECKOUT_BUTTON = "//button[@class='btn btn_action btn_medium checkout_button ' and contains(text(), 'Checkout')]"


class ShoppingCartPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ShoppingCartLocators()

    def verify_opening_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(
            self.page.locator(self.locators.SAUCE_LABS_BACKPACK_PRODUCT)
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.SAUCE_LABS_BACKPACK_PRODUCT)
        ).to_be_enabled()
        expect(self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT)).to_be_visible()
        expect(self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT)).to_be_enabled()
        expect(
            self.page.locator(self.locators.CONTINUE_SHOPPING_BUTTON)
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.CONTINUE_SHOPPING_BUTTON)
        ).to_be_enabled()

    def click_checkout_button(self):
        expect(self.page.locator(self.locators.CHECKOUT_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.CHECKOUT_BUTTON)).to_be_enabled()
        self.page.click(self.locators.CHECKOUT_BUTTON)
