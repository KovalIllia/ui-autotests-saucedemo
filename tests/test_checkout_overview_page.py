from playwright.sync_api import expect


def test_checkout_overview_page(checkout_overview_page):
    checkout_overview_page.click_finish_button()
    expect(checkout_overview_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")