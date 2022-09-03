import time
from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def scroll_imgs(self):
        count_imgs = self.browser.find_elements(*ProductPageLocators.COUNT_IMGS["xpath"])
        #print(f"len count_imgs: {len(count_imgs) + 1}")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME["xpath"]).text
        #print(f"product_name: {product_name}")
        main_img = self.browser.find_element(*ProductPageLocators.ITEM_IMGS["xpath"]).click()
        time.sleep(0.5)
        count_imgs_in_holder = self.browser.find_element(*ProductPageLocators.COUNT_IMGS_IN_HOLDER["xpath"]).text
        #print(f"count_imgs_in_holder: {count_imgs_in_holder[5:]}")
        product_name_in_holder = self.browser.find_element(*ProductPageLocators.IMG_NAME["xpath"]).text
        #print(f"product_name_in_holder: {product_name_in_holder}")
        scroll_next = self.browser.find_element(*ProductPageLocators.SCROLL_IMG_NEXT["xpath"])
        count = 0
        for i in range(len(count_imgs) + 1):
            scroll_next.click()
            count += 1

        assert count == len(count_imgs) + 1, f"{count} != {len(count_imgs)} User doesn`t see all images"
        assert len(count_imgs) + 1 == int(count_imgs_in_holder[5:]), f"{len(count_imgs)} != {int(count_imgs_in_holder[5:])} Any pictures are lost"
        assert product_name == product_name_in_holder, "The names are different"

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME["xpath"]).text
        imgs = self.browser.find_element(*ProductPageLocators.ITEM_IMGS["xpath"]).click()
        time.sleep(1)
        img_name = self.browser.find_element(*ProductPageLocators.IMG_NAME["xpath"]).text
        assert product_name == img_name, "This img is not from this product"


    def click_like(self):
        self.browser.find_element(*ProductPageLocators.LIKE["xpath"]).click()
        success_text = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT["xpath"])
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(success_text))


    def click_compare(self):
        self.browser.find_element(*ProductPageLocators.COMPARE).click()
        success_text = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT["xpath"])
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(success_text))

    def set_quantity_of_product(self, quantity: int):
        input_area = self.browser.find_element(*ProductPageLocators.QUANTITY["xpath"])
        input_area.clear()
        input_area.send_keys(quantity)

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART["xpath"])
        add_to_cart.click()
        WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-check-circle")))

    def run_by_product_tabs(self):
        nav_tabs = self.browser.find_elements(*ProductPageLocators.ITEM_NAV["xpath"])
        for item in nav_tabs:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()
