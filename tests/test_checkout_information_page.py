from playwright.sync_api import expect

from utils.user_credentials import UserCredentialForDelivery


def test_checkout_information_page(checkout_information_page):
    first_name = UserCredentialForDelivery.STANDARD_USER_FIRST_NAME
    last_name = UserCredentialForDelivery.STANDARD_USER_LAST_NAME
    zip_code = UserCredentialForDelivery.STANDARD_USER_ZIP_CODE

    checkout_information_page.fill_first_name(first_name)
    checkout_information_page.fill_last_name(last_name)
    checkout_information_page.fill_zip_code(zip_code)
    checkout_information_page.click_continue_button()
    expect(checkout_information_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")


