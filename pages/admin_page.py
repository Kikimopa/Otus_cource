from pages.base_page import BasePage
from locators.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):


    def admin_authorization(self):
        self.browser.find_element(*AdminPageLocators.LOGIN).send_keys("admin")
        self.browser.find_element(*AdminPageLocators.PASSWORD).send_keys("admin")
        self.browser.find_element(*AdminPageLocators.SUBMIT).click()

    def user_is_in_admin_page(self):
        logo = self.browser.find_element(*AdminPageLocators.LOGO)
        assert logo, "User is not connected to admin page"

    def go_to_products_page(self):
        self.browser.get(
            "http://192.168.218.128/opencart/upload/admin/index.php?route=catalog/product&user_token=SNbLHHu2JlyDgfl0Qpgb3BdoiK6cbUSV")

    def click_to_add_new_product(self):
        self.browser.find_element(*AdminPageLocators.ADD_PRODUCT).click()

    def check_product_page(self):
        add_product_title = self.browser.find_element(*AdminPageLocators.ADD_PRODUCT_TITLE).text
        assert add_product_title == "Add Product", "User can not add new product"

    def user_input_new_product(self, name, description, meta_tags, model):
        self.browser.find_element(*AdminPageLocators.INPUT_PRODUCT_NAME).send_keys(name)
        self.browser.find_element(*AdminPageLocators.PRODUCT_DESCRIPTION).send_keys(description)
        self.browser.find_element(*AdminPageLocators.META_TAG_TITLE).send_keys(meta_tags)
        self.browser.find_element(*AdminPageLocators.DATA).click()
        self.browser.find_element(*AdminPageLocators.MODEL).send_keys(model)


    def product_is_save(self):
        success_text = self.browser.find_element(*AdminPageLocators.SUCCESS).text
        assert success_text == "Success: You have modified products!", "User don`t add new product"

    def click_to_product_page(self):
        # product_menu =
        self.browser.find_element(*AdminPageLocators.PRODUCTS).click()
        # product_menu[1].click()

    def delete_product(self):
        self.browser.find_element(*AdminPageLocators.CHECKBOX).click()
        self.browser.find_element(*AdminPageLocators.DELETE_BUTTON).click()
        alert = self.browser.switch_to.alert
        alert.accept()
        success_text = self.browser.find_element(*AdminPageLocators.SUCCESS).text
        assert success_text == "Success: You have modified products!", "User don`t delete product"

