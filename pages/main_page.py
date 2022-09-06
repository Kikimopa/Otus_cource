import time
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.product_page_locators import ProductPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def open_main_page(self):
        self.browser.get("https://demo.opencart.com/")

    def check_main_page(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO["xpath"]).get_attribute("title")
        assert logo == "Your Store", 'It is not opencart homepage'

    def check_currency(self):
        self.browser.find_element(*MainPageLocators.CURRENCY["xpath"]).click()
        cur_list = self.browser.find_element(*MainPageLocators.CUR_LIST["xpath"])
        assert cur_list, "There is no currency here"


    def send_on_to_search_input(self, text):
        search = self.browser.find_element(*MainPageLocators.SEARCH_INPUT["xpath"])
        search.clear()
        search.send_keys(text)

    def search_product(self, text):
        search = self.browser.find_element(*MainPageLocators.SEARCH_INPUT["xpath"])
        search.clear()
        search.send_keys(text)
        self.browser.find_element(*MainPageLocators.SEARCH_BUTTON["xpath"]).click()
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(*MainPageLocators.SEARCH_ERROR["xpath"]))


    def run_by_nav_bar(self):
        nav_bar = self.browser.find_elements(*MainPageLocators.NAV_BAR["xpath"])
        for item in nav_bar:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()

    def run_by_top_links(self):
        top_links = self.browser.find_elements(*MainPageLocators.TOP_LINKS["xpath"])
        for item in top_links:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()

    def click_to_cart(self):
        cart = self.browser.find_element(*MainPageLocators.CART["xpath"])
        cart.click()

    def click_to_product(self, index):
        product_name = self.browser.find_elements(*MainPageLocators.PRODUCT_NAME["xpath"])[index].text
        print(product_name)
        product = self.browser.find_elements(*MainPageLocators.PRODUCT["xpath"])[index]
        product.click()
        name_after_click = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME["xpath"]).text
        assert product_name == name_after_click, "There is different products"


    def add_product_to_cart(self):
        self.browser.execute_script("scrollTo(100, 1500)")
        # fotter = self.browser.find_element(*MainPageLocators.FOOTER["xpath"])
        # ActionChains(self.browser).move_to_element(fotter).perform()
        time.sleep(.5)
        self.browser.find_element(*MainPageLocators.ADD_TO_CART["xpath"]).click()
        time.sleep(.5)
        success_text = self.browser.find_element(*MainPageLocators.SUCCESS_TEXT["xpath"])
        assert success_text, "User doesn`t add product ro cart"
