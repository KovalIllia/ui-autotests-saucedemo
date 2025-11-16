def test_checkout_complete_page(complete_page):
    complete_page.verify_complete_logo()
    complete_page.verify_success_message()
    complete_page.verify_back_home_button()