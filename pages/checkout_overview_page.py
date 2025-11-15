from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure


class CheckoutOverviewLocators:
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(),'Checkout: Overview')]"
    FIRST_CHOSEN_PRODUCT = "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]"
    SECOND_CHOSEN_PRODUCT = "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Bike Light')]"
    PAYMENT_INFORMATION_FIELD = "//div[@class='summary_info_label' and @data-test='payment-info-label' and contains(text(), 'Payment Information:')]"
    SHIPPING_INFORMATION_FIELD = "//div[@class='summary_info_label' and @data-test='shipping-info-label' and contains(text(), 'Shipping Information:')]"
    PRICE_TOTAL_INFORMATION_FIELD = "//div[@class='summary_info_label' and @data-test='total-info-label' and contains(text(), 'Price Total')]"
    CANCEL_BUTTON = "//button[@class='btn btn_secondary back btn_medium cart_cancel_link' and @data-test='cancel']"
    FINISH_BUTTON = "//button[@class='btn btn_action btn_medium cart_button' and @data-test='finish' ]"


class CheckoutOverviewPage(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CheckoutOverviewLocators

    def verify_opening_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_have_text(
            "Checkout: Overview"
        )
        expect(self.page.locator(self.locators.FIRST_CHOSEN_PRODUCT)).to_be_visible()
        expect(self.page.locator(self.locators.FIRST_CHOSEN_PRODUCT)).to_have_text(
            "Sauce Labs Backpack"
        )
        expect(self.page.locator(self.locators.SECOND_CHOSEN_PRODUCT)).to_be_visible()
        expect(self.page.locator(self.locators.SECOND_CHOSEN_PRODUCT)).to_have_text(
            "Sauce Labs Bike Light"
        )
        expect(
            self.page.locator(self.locators.PAYMENT_INFORMATION_FIELD)
        ).to_be_visible()
        expect(self.page.locator(self.locators.PAYMENT_INFORMATION_FIELD)).to_have_text(
            "Payment Information:"
        )
        expect(
            self.page.locator(self.locators.SHIPPING_INFORMATION_FIELD)
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.SHIPPING_INFORMATION_FIELD)
        ).to_have_text("Shipping Information:")
        expect(
            self.page.locator(self.locators.PRICE_TOTAL_INFORMATION_FIELD)
        ).to_be_visible()
        expect(
            self.page.locator(self.locators.PRICE_TOTAL_INFORMATION_FIELD)
        ).to_have_text("Price Total")
        expect(self.page.locator(self.locators.CANCEL_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.FINISH_BUTTON)).to_be_visible()

    def click_finish_button(self):
        expect(self.page.locator(self.locators.FINISH_BUTTON)).to_be_visible()
        expect(self.page.locator(self.locators.FINISH_BUTTON)).to_be_enabled()
        self.page.click(self.locators.FINISH_BUTTON)
