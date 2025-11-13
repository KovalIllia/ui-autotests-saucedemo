from playwright.sync_api import expect


def test_checking_shopping_cart_page(shopping_cart_page):

    shopping_cart_page.click_checkout_button()
    expect(shopping_cart_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")