from selenium import webdriver
from main_page_shop import MainPageShop
from catalog_page import CatalogPage
from cart_page import CartPage
from checkout_1_page import Checkout1Page
from checkout_2_page import Checkout2Page


def test_shop():
    browser = webdriver.Chrome()
    main_page = MainPageShop(browser)
    main_page.login('standard_user', 'secret_sauce')
    
    catalog_page = CatalogPage(browser)
    catalog_page.add_product_to_cart()
    catalog_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_1_page = Checkout1Page(browser)
    checkout_1_page.fill_form('Denis', 'Klyavin', '600029')
    checkout_1_page.click_continue()
    
    checkout_2_page = Checkout2Page(browser)
    total = checkout_2_page.get_total()
    browser.quit()

    assert total == '$58.29', 'Total is not correct'