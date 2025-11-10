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

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
