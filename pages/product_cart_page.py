from base_page import BasePage
from locators.item_locators import ItemCardLocators
from selenium.webdriver.common.action_chains import ActionChains

class ProductCartPage(BasePage):

    def scroll_imgs(self):
        item_imgs = self.browser.find_elements(*ItemCardLocators.ITEM_IMGS)
        for item in item_imgs:
            item.click()

    def click_like_and_compresion(self):
        buttons = self.browser.find_elements(*ItemCardLocators.BUTTONS)
        for button in buttons:
            button.click()

    def set_quantity_of_product(self, quantity: int):
        input_area = self.browser.find_element(*ItemCardLocators.QUANTITY)
        input_area.clear()
        input_area.send_keys(quantity)

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ItemCardLocators.ADD_TO_CART)
        add_to_cart.click()

    def run_by_nav_tabs(self):
        nav_tabs = self.browser.find_elements(*ItemCardLocators.ITEM_NAV)
        for item in nav_tabs:
            ActionChains(self.browser).move_to_element(item).pause(1).perform()