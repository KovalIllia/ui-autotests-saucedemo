from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect

class ProductsPageLocators:
    LOGIN_PAGE_TITTLE = "//div[@class='login_logo']"
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(), 'Products')]"
    SAUCE_LABS_BACKPACK = "//div[@class='inventory_item_name ' and @data-test='inventory-item-name' and contains(text(), 'Sauce Labs Backpack')]"
    SAUCE_LABS_BIKE_LIGHT = "//div[@class='inventory_item_name ' and @data-test='inventory-item-name' and contains(text(), 'Sauce Labs Bike Light')]"
    SHOPPING_CART_BUCKET = "//span[@class='shopping_cart_badge' and @data-test='shopping-cart-badge']"


class ProductsPage(LoginPage):

    def __init__(self, page= Page):
        super().__init__(page)
        self.locators=ProductsPageLocators()

    def verify_opening_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.SAUCE_LABS_BACKPACK)).to_be_visible()
        expect(self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT)).to_be_visible()
        expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_be_visible()

    def get_first_order(self):
        self.page.click(self.locators.SAUCE_LABS_BACKPACK)
        expect(self.page.locator(self.locators.SAUCE_LABS_BACKPACK)).to_be_enabled()

    def get_second_order(self):
        self.page.click(self.locators.SAUCE_LABS_BIKE_LIGHT)
        expect(self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT)).to_be_enabled()

    def shopping_cart_backet(self):
        self.page.click(self.locators.SHOPPING_CART_BUCKET)
        expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_be_enabled()