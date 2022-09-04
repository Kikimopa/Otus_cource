import time
import allure
from pages.admin_page import AdminPage
import pytest
from random import randint



@allure.severity(allure.severity_level.CRITICAL)
def test_admin_can_login(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.is_in_admin_page()

@allure.severity(allure.severity_level.TRIVIAL)
def test_admin_can_go_to_product_page(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()

@allure.severity(allure.severity_level.CRITICAL)
def test_admin_can_go_to_add_new_product_page(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()
    page.click_to_add_new_product()
    page.check_product_page()

@allure.severity(allure.severity_level.TRIVIAL)
def test_admin_can_run_by_nav_tabs(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()
    time.sleep(0.1)
    page.click_to_add_new_product()
    page.run_by_nav_tabs()

@allure.severity(allure.severity_level.CRITICAL)
def test_admin_can_add_new_product(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()
    time.sleep(0.1)
    page.click_to_add_new_product()
    name = "Ноутбук DIGMA EVE 15C419"
    description = "Ноутбук DIGMA EVE 15C419 1920x1080, Intel Celeron N4020 1.1 ГГц, SSD 128 ГБ, Intel UHD Graphics 600, Windows 10 Home, ES5065EW, темно-серый"
    meta_tags = "Ноутбук DIGMA EVE"
    model = "15C419"
    page.input_new_product(name, description, meta_tags, model)
    page.click_to_save_button()
    page.product_is_save()

@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize('num_product', [randint(1, 14)])
def test_admin_can_copy_product(browser, num_product):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()
    page.copy_product(num_product)

@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.parametrize('num_product', [randint(1, 14)])
def test_admin_can_delete_product(browser, num_product):
    page = AdminPage(browser)
    page.open_admin_page()
    page.admin_authorization()
    page.go_to_products_page()
    page.delete_product(num_product)

@allure.severity(allure.severity_level.BLOCKER)
def test_admin_can_download_img(browser):
    page = AdminPage(browser)
    page.open_admin_page()
    page.go_to_download_page()
    page.admin_authorization()
    page.add_new_download("selenium", "D:\otus_course\Otus_cource\data\selenium.png", "abcdefgh")


