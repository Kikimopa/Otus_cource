import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):

    def check_main_page(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        assert logo.getattribut("title") == "Your Store", 'It is not opencart homepage'

    def check_currency(self):
        self.browser.find_element(*MainPageLocators.CURRENCY).click()
        cur_list = self.browser.find_element(*MainPageLocators.CUR_LIST)
        assert cur_list, "There is no currency here"


    def send_on_to_search_input(self, text):
        search = self.browser.find_element(*MainPageLocators.SEARCH_INPUT)
        search.clear()
        search.send_keys(text)



    def run_by_nav_bar(self):
        nav_bar = self.browser.find_elements(*MainPageLocators.NAV_BAR)
        for item in nav_bar:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()

    def run_by_top_links(self):
        top_links = self.browser.find_elements(*MainPageLocators.TOP_LINKS)
        for item in top_links:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()

    def click_to_cart(self):
        cart = self.browser.find_element(*MainPageLocators.CART)
        cart.click()

    def click_to_product(self, number):
        index = number - 1
        product = self.browser.find_elements(*MainPageLocators.PRODUCT)[index]
        product.click()

    def add_product_to_cart(self):
        self.browser.find_element(*MainPageLocators.ADD_TO_CART).click()
