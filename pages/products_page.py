from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure


class ProductsPageLocators:
    # LOGIN_PAGE_TITTLE = "//div[@class='login_logo']"
    PAGE_TITTLE = (
        "//span[@class='title' and @data-test='title' and contains(text(), 'Products')]"
    )
    SAUCE_LABS_BACKPACK = "//div[@class='inventory_item_name ' and @data-test='inventory-item-name' and contains(text(), 'Sauce Labs Backpack')]"
    SAUCE_LABS_BIKE_LIGHT = "//div[@class='inventory_item_name ' and @data-test='inventory-item-name' and contains(text(), 'Sauce Labs Bike Light')]"
    SHOPPING_CART_BUCKET = (
        "//span[@class='shopping_cart_badge' and @data-test='shopping-cart-badge']"
    )
    SAUCE_LABS_BACKPACK_BUTTON = "//button[@class='btn btn_primary btn_small btn_inventory ' and @data-test='add-to-cart-sauce-labs-backpack' and @name='add-to-cart-sauce-labs-backpack']"
    SAUCE_LABS_BIKE_LIGHT_BUTTON = "//button[@class='btn btn_primary btn_small btn_inventory ' and @data-test='add-to-cart-sauce-labs-bike-light' and @name='add-to-cart-sauce-labs-bike-light']"


class ProductsPage(LoginPage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ProductsPageLocators()

    def verify_opening_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.SAUCE_LABS_BACKPACK)).to_be_visible()
        expect(self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT)).to_be_visible()
        # expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_be_visible()

    @allure.step("Add first item to cart")
    def get_first_order(self):
        expect(
            self.page.locator(self.locators.SAUCE_LABS_BACKPACK_BUTTON)
        ).to_be_enabled()
        self.page.click(self.locators.SAUCE_LABS_BACKPACK_BUTTON)
        expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_have_text("1")

    @allure.step("Add second item to cart")
    def get_second_order(self):
        expect(
            self.page.locator(self.locators.SAUCE_LABS_BIKE_LIGHT_BUTTON)
        ).to_be_enabled()
        self.page.click(self.locators.SAUCE_LABS_BIKE_LIGHT_BUTTON)
        expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_have_text("2")

    def shopping_cart_backet(self):
        expect(self.page.locator(self.locators.SHOPPING_CART_BUCKET)).to_be_enabled()
        self.page.click(self.locators.SHOPPING_CART_BUCKET)
