from playwright.sync_api import expect


def test_add_items_to_cart(products_page_part_for_test):

    products_page_part_for_test.get_first_order()
    products_page_part_for_test.get_second_order()
    products_page_part_for_test.shopping_cart_backet()
    expect(products_page_part_for_test.page).to_have_url("https://www.saucedemo.com/cart.html")