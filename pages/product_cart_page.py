import time
from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductCartPage(BasePage):

    def scroll_imgs(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        imgs = self.browser.find_elements(*ProductPageLocators.ITEM_IMGS)[0]
        count_imgs = imgs.find_elements(*ProductPageLocators.COUNT_IMGS)
        imgs = self.browser.find_element(*ProductPageLocators.ITEM_IMGS).click()
        scroll = self.browser.find_element(*ProductPageLocators.SCROLL_IMG)
        img_name = self.browser.find_element(*ProductPageLocators.IMG_NAME).text
        count = 0
        for i in range(len(count_imgs) - 1):
            scroll.click()
            count += 1
        assert count == len(count_imgs) - 1, "User doesn`t see all images"

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        imgs = self.browser.find_element(*ProductPageLocators.ITEM_IMGS).click()
        time.sleep(1)
        img_name = self.browser.find_element(*ProductPageLocators.IMG_NAME).text
        assert product_name == img_name, "This img is not from this product"


    def click_like(self):
        self.browser.find_element(*ProductPageLocators.LIKE).click()
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))


    def click_compare(self):
        self.browser.find_element(*ProductPageLocators.COMPARE).click()
        # time.sleep(30)
        WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-exclamation-circle")))

    def set_quantity_of_product(self, quantity: int):
        input_area = self.browser.find_element(*ProductPageLocators.QUANTITY)
        input_area.clear()
        input_area.send_keys(quantity)

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
        WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-check-circle")))

    def run_by_product_tabs(self):
        nav_tabs = self.browser.find_elements(*ProductPageLocators.ITEM_NAV)
        for item in nav_tabs:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()
