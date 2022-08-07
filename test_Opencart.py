import time

import pytest
from selenium.webdriver.common.by import By
from .locators.MainPageLocators import MainPageLocators
from .locators.ItemCardLocators import ItemCardLocators
from selenium.webdriver.common.action_chains import ActionChains


url = "http://192.168.218.128/opencart/upload/"

def test_01(browser):

    h1 = browser.find_element(By.TAG_NAME, "h1").text
    assert h1 == "Your Store", 'It is not opencart homepage'

def test_find_input_search(browser):

    search = browser.find_element(*MainPageLocators.SEARCH_INPUT)
    search.send_keys("Iphone")


def test_run_by_nav_bar(browser):

    nav_bar = browser.find_elements(*MainPageLocators.NAV_BAR)
    for item in nav_bar:
        ActionChains(browser).move_to_element(item).pause(1).perform()

def test_run_top_links(browser):

    top_links = browser.find_elements(*MainPageLocators.TOP_LINKS)
    for item in top_links:
        ActionChains(browser).move_to_element(item).pause(1).perform()

def test_click_to_cart(browser):

    cart = browser.find_element(*MainPageLocators.CART).click()

def test_click_to_item(browser):

    product = browser.find_element(*MainPageLocators.PRODUCT).click()



def test_scroll_imgs(browser):
    product = browser.find_element(*MainPageLocators.PRODUCT).click()
    item_imgs = browser.find_elements(*ItemCardLocators.ITEM_IMGS)
    for item in item_imgs:
        item.click()

def test_run_by_nav_tabs(browser):
    product = browser.find_element(*MainPageLocators.PRODUCT).click()
    nav_tabs = browser.find_elements(*ItemCardLocators.ITEM_NAV)
    for item in nav_tabs:
        ActionChains(browser).move_to_element(item).pause(1).perform()

def test_clcik_like_and_comparison(browser):
    product = browser.find_element(*MainPageLocators.PRODUCT).click()
    buttons = browser.find_elements(*ItemCardLocators.BUTTONS)
    for button in buttons:
        button.click()

def test_set_quantity_of_product(browser):
    product = browser.find_element(*MainPageLocators.PRODUCT).click()
    quantity = browser.find_element(*ItemCardLocators.QUANTITY)
    quantity.send_keys("123")

def test_add_product_to_cart(browser):
    product = browser.find_element(*MainPageLocators.PRODUCT).click()
    add_to_cart = browser.find_element(*ItemCardLocators.ADD_TO_CART)
    add_to_cart.click()


if __name__ == "__main__":
    pytest.main()