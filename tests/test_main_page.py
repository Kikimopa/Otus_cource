import allure
import pytest
from pages.main_page import MainPage
import random



@allure.severity(allure.severity_level.MINOR)
def test_check_main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.check_main_page()

@allure.severity(allure.severity_level.TRIVIAL)
def test_check_currency(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.check_currency()

@allure.severity(allure.severity_level.MINOR)
def test_find_input_search(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.send_on_to_search_input("Iphone")

@allure.severity(allure.severity_level.NORMAL)
def test_run_by_nav_bar(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.run_by_nav_bar()

@allure.severity(allure.severity_level.NORMAL)
def test_run_top_links(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.run_by_top_links()

@allure.severity(allure.severity_level.CRITICAL)
def test_click_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.click_to_cart()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('num_product', [random.randint(1, 4)])
def test_click_to_product(browser, num_product):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.click_to_product(num_product)

@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.add_product_to_cart()


if __name__ == "__main__":
    pytest.main()