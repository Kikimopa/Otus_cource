import time

import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains



def test_check_main_page(browser):
    main_page = MainPage(browser)
    main_page.check_main_page()

def test_check_currency(browser):
    main_page = MainPage(browser)
    main_page.check_currency()


def test_find_input_search(browser):
    main_page = MainPage(browser)
    main_page.send_on_to_search_input("Iphone")


def test_run_by_nav_bar(browser):
    main_page = MainPage(browser)
    main_page.run_by_nav_bar()


def test_run_top_links(browser):
    main_page = MainPage(browser)
    main_page.run_by_top_links()


def test_click_to_cart(browser):
    main_page = MainPage(browser)
    main_page.click_to_cart()


def test_click_to_product(browser):
    main_page = MainPage(browser)
    main_page.click_to_product(1)


def test_add_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.add_product_to_cart()


if __name__ == "__main__":
    pytest.main()