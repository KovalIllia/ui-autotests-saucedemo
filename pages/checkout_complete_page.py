from pages.login_page import LoginPage
from playwright.sync_api import Browser, Page, expect
import allure

class CheckoutCompleteLocators:
    PAGE_TITTLE = "//span[@class='title' and @data-test='title' and contains(text(),'Checkout: Complete!')]"
    COMPLETE_PAGE_LOGO="//img[@alt='Pony Express' and @data-test='pony-express']"
    COMPLETE_HEADER="//h2[@class='complete-header' and @data-test='complete-header']"
    COMPLETE_TEXT="//div[@class='complete-text' and @data-test='complete-text' and contains(text(), 'Your order has been dispatched, and will arrive just as fast as the pony can get there!')]"
    BACK_HOME_PAGE="//button[@class='btn btn_primary btn_small' and @data-test='back-to-products']"

class CheckoutCompletePage(LoginPage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.locators=CheckoutCompleteLocators

    def verify_opening_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    def verify_page_loaded(self):
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.locators.PAGE_TITTLE)).to_be_visible()
        expect(self.page.locator(self.locators.COMPLETE_PAGE_LOGO)).to_be_visible()
        expect(self.page.locator(self.locators.COMPLETE_HEADER)).to_be_visible()
        expect(self.page.locator(self.locators.COMPLETE_TEXT)).to_be_visible()
        expect(self.page.locator(self.locators.BACK_HOME_PAGE)).to_be_visible()

    def verify_complete_logo(self):
        expect(self.page.locator(self.locators.COMPLETE_PAGE_LOGO)).to_have_attribute("alt", "Pony Express")
        expect(self.page.locator(self.locators.COMPLETE_PAGE_LOGO)).to_have_attribute("data-test", "pony-express")

    @allure.step("Verify success message")
    def verify_success_message(self):
        expect(self.page.locator(self.locators.COMPLETE_HEADER)).not_to_be_empty()
        expect(self.page.locator(self.locators.COMPLETE_HEADER)).to_have_text("Thank you for your order!")
        expect(self.page.locator(self.locators.COMPLETE_TEXT)).to_contain_text("Your order has been dispatched")

    def verify_back_home_button(self):
        expect(self.page.locator(self.locators.BACK_HOME_PAGE)).to_be_enabled()
        self.page.click(self.locators.BACK_HOME_PAGE)