import time
import allure
import pytest
import random
from pages.product_page import ProductPage
from pages.main_page import MainPage


@allure.severity(allure.severity_level.NORMAL)
class TestProductPage:

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    def test_run_by_imgs(self, browser, num_product):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.scroll_imgs()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    def test_check_product_name(self, browser,num_product):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.check_product_name()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    def test_add_to_wish_list(self, browser, num_product):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.click_like()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    def test_add_to_compare(self, browser, num_product):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.click_compare()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    @pytest.mark.parametrize('value', [random.randint(0, 999)])
    def test_set_quantity(self, browser, num_product, value):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.set_quantity_of_product(value)

    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    @pytest.mark.parametrize('value', [random.randint(0, 999)])
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_any_product_to_cart(self, browser, num_product, value):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.set_quantity_of_product(value)
        product_page.add_to_cart()

    @pytest.mark.parametrize('num_product', [random.randint(0, 3)])
    @allure.severity(allure.severity_level.MINOR)
    def test_run_by_product_tabs(self, browser, num_product):
        main_page = MainPage(browser)
        main_page.open_main_page()
        main_page.click_to_product(num_product)
        product_page = ProductPage(browser)
        product_page.run_by_product_tabs()

