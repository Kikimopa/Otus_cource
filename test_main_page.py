import time
import pytest
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, ItemCardLocators
from selenium.webdriver.common.action_chains import ActionChains



def test_01(browser_mainPage):
    h1 = browser_mainPage.find_element(By.TAG_NAME, "h1").text
    assert h1 == "Your Store", 'It is not opencart homepage'


def test_find_input_search(browser_mainPage):
    search = browser_mainPage.find_element(*MainPageLocators.SEARCH_INPUT)
    search.send_keys("Iphone")


def test_run_by_nav_bar(browser_mainPage):
    nav_bar = browser_mainPage.find_elements(*MainPageLocators.NAV_BAR)
    for item in nav_bar:
        ActionChains(browser_mainPage).move_to_element(item).pause(1).perform()


def test_run_top_links(browser_mainPage):
    top_links = browser_mainPage.find_elements(*MainPageLocators.TOP_LINKS)
    for item in top_links:
        ActionChains(browser_mainPage).move_to_element(item).pause(1).perform()


def test_click_to_cart(browser_mainPage):
    cart = browser_mainPage.find_element(*MainPageLocators.CART)
    cart.click()


def test_click_to_item(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()


def test_scroll_imgs(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()
    item_imgs = browser_mainPage.find_elements(*ItemCardLocators.ITEM_IMGS)
    for item in item_imgs:
        item.click()


def test_run_by_nav_tabs(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()
    nav_tabs = browser_mainPage.find_elements(*ItemCardLocators.ITEM_NAV)
    for item in nav_tabs:
        ActionChains(browser_mainPage).move_to_element(item).pause(1).perform()


def test_click_like_and_comparison(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()
    buttons = browser_mainPage.find_elements(*ItemCardLocators.BUTTONS)
    for button in buttons:
        button.click()


def test_set_quantity_of_product(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()
    quantity = browser_mainPage.find_element(*ItemCardLocators.QUANTITY)
    quantity.clear()
    quantity.send_keys("123")


def test_add_product_to_cart(browser_mainPage):
    product = browser_mainPage.find_element(*MainPageLocators.PRODUCT)
    product.click()
    add_to_cart = browser_mainPage.find_element(*ItemCardLocators.ADD_TO_CART)
    add_to_cart.click()


if __name__ == "__main__":
    pytest.main()
