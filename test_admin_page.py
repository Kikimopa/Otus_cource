import time
from selenium.webdriver.common.action_chains import ActionChains
from .pages.admin_page import AdminPage
from .pages.locators import AdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_user_can_login(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.admin_authorization()
    page.user_is_in_admin_page()

# def test_user_can_go_to_product_page(browser_adminPage):
#     page = AdminPage(browser_adminPage)
#     page.go_to_admin_page()
#     page.admin_authorization()
#     page.click_to_product_page()
#     time.sleep(5)


def test_user_can_go_to_add_new_product_page(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.go_to_products_page()
    page.admin_authorization()
    page.click_to_add_new_product()
    page.check_product_page()


def test_user_can_run_by_nav_tabs(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.go_to_products_page()
    page.admin_authorization()
    page.click_to_add_new_product()
    nav_tabs = browser_adminPage.find_elements(*AdminPageLocators.NAV_MENU)
    for item in nav_tabs:
        ActionChains(browser_adminPage).move_to_element(item).pause(0.5).perform()



def test_user_can_add_new_product(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.go_to_products_page()
    page.admin_authorization()
    page.click_to_add_new_product()
    time.sleep(2)
    name = "Ноутбук DIGMA EVE 15C419"
    description = "Ноутбук DIGMA EVE 15C419 1920x1080, Intel Celeron N4020 1.1 ГГц, SSD 128 ГБ, Intel UHD Graphics 600, Windows 10 Home, ES5065EW, темно-серый"
    meta_tags = "Ноутбук DIGMA EVE"
    model = "15C419"
    page.user_input_new_product(name, description, meta_tags, model)
    save_button = browser_adminPage.find_element(*AdminPageLocators.SAVE_BUTTON).click()
    page.product_is_save()


def test_user_can_copy_product(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.admin_authorization()
    page.go_to_products_page()

def test_user_can_delete_product(browser_adminPage):
    page = AdminPage(browser_adminPage)
    page.go_to_admin_page()
    page.go_to_products_page()
    page.admin_authorization()
    page.delete_product()
