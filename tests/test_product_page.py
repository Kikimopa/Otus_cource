from pages.product_page import ProductPage
from pages.main_page import MainPage

def test_run_by_imgs(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.scroll_imgs()

def test_check_product_name(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.check_product_name()

def test_add_to_wish_list(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.click_like()

def test_add_to_compare(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.click_compare()


def test_set_quantity(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.set_quantity_of_product(999)

def test_add_any_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.set_quantity_of_product(23)
    product_page.add_to_cart()

def test_run_by_product_tabs(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)
    product_page = ProductPage(browser)
    product_page.run_by_product_tabs()
