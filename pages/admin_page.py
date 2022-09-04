import time
from pages.base_page import BasePage
from locators.admin_page_locators import AdminPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):

    def open_admin_page(self):
        #self.browser.get("https://demo.opencart.com/admin/")
        self.browser.get("http://192.168.218.128/opencart/upload/admin/")

    def admin_authorization(self):
        self.browser.find_element(*AdminPageLocators.LOGIN["name"]).send_keys("admin")
        self.browser.find_element(*AdminPageLocators.PASSWORD["name"]).send_keys("admin")
        self.browser.find_element(*AdminPageLocators.SUBMIT["tag"]).click()


    def is_in_admin_page(self):
        logo = self.browser.find_element(*AdminPageLocators.LOGO)
        assert logo, "User is not connected to admin page"

    def go_to_products_page(self):
        self.browser.find_element(*AdminPageLocators.CATALOG["xpath"]).click()
        time.sleep(0.5)
        self.browser.find_element(*AdminPageLocators.PRODUCTS["xpath"]).click()
        title = self.browser.find_element(*AdminPageLocators.PRODUCT_TITLE["xpath"]).text
        assert title == "Products", "User doesn`t in product catalog"


    def click_to_add_new_product(self):
        self.browser.find_element(*AdminPageLocators.ADD_PRODUCT["xpath_my"]).click()

    def check_product_page(self):
        add_product_title = self.browser.find_element(*AdminPageLocators.ADD_PRODUCT_TITLE["xpath_my"]).text
        assert add_product_title == "Add Product", "User can not add new product"

    def input_new_product(self, name, description, meta_tags, model):
        self.browser.find_element(*AdminPageLocators.INPUT_PRODUCT_NAME["xpath"]).send_keys(name)
        self.browser.find_element(*AdminPageLocators.PRODUCT_DESCRIPTION["xpath_my"]).send_keys(description)
        self.browser.find_element(*AdminPageLocators.META_TAG_TITLE["xpath"]).send_keys(meta_tags)
        self.browser.find_element(*AdminPageLocators.DATA["xpath"]).click()
        self.browser.find_element(*AdminPageLocators.MODEL["xpath"]).send_keys(model)


    def product_is_save(self):
        success_text = self.browser.find_element(*AdminPageLocators.SUCCESS).text
        assert success_text == "Success: You have modified products!", "User don`t add new product"

    def click_to_save_button(self):
        self.browser.find_element(*AdminPageLocators.SAVE_BUTTON["xpath"]).click()

    def delete_product(self, number):
        index = number - 1
        if index > 0:
            check_box = self.browser.find_elements(*AdminPageLocators.CHECKBOX["xpath"])
            check_box[index].click()
            self.browser.find_element(*AdminPageLocators.DELETE_BUTTON["xpath"]).click()
            alert = self.browser.switch_to.alert
            alert.accept()
            success_text = self.browser.find_element(*AdminPageLocators.SUCCESS["xpath"]).text
            assert success_text == "Success: You have modified products!", "User doesn`t delete product"
        else:
            print("Don`t do it!!!")

    def go_to_download_page(self):
        self.browser.find_element(*AdminPageLocators.DOWNLOADS["xpath"]).click()

    def add_new_download(self, name, path, mask):
        # file_dir_name = os.path.dirname(__file__)
        # file_name = os.path.join(file_dir_name, "selenium.png")
        buttons = self.browser.find_elements(*AdminPageLocators.BUTTONS)[-1]
        buttons.find_elements(*AdminPageLocators.ADD_DOWNLOAD_BUTTON)[0].click()
        download_name = self.browser.find_element(*AdminPageLocators.DOWNLOAD_NAME)
        download_name.send_keys(name)
        self.browser.execute_script(
            """var f = document.createElement("form");
            f.id = "form-upload";
            f.style.display = "block";
            f.enctype = "multipart/form-data";
            inp = document.createElement("input");
            inp.type = "file";
            inp.name = "file";
            f.appendChild(inp);
            body = document.getElementsByTagName("body")[0];
            body.insertBefore(f, body.firstChild);
            """)
        download_area = self.browser.find_element(*AdminPageLocators.DOWNLOAD_AREA)
        download_area.clear()
        download_area.send_keys(path)
        download_file_name = self.browser.find_element(*AdminPageLocators.DOWNLOAD_FILE_NAME)
        download_file_name.send_keys(name)
        downLoad_mask = self.browser.find_element(*AdminPageLocators.DOWNLOAD_MASK)
        downLoad_mask.send_keys(mask)
        self.browser.find_element(*AdminPageLocators.SAVE_BUTTON).click()
        text_danger = self.browser.find_element(*AdminPageLocators.ATTANTION)
        assert text_danger, "User add new file"

    def run_by_nav_tabs(self):
        nav_tabs = self.browser.find_elements(*AdminPageLocators.NAV_MENU["xpath"])
        for item in nav_tabs:
            ActionChains(self.browser).move_to_element(item).pause(0.5).perform()

    def copy_product(self, number):
        index = number - 1
        if index > 0:
            check_box = self.browser.find_elements(*AdminPageLocators.CHECKBOX["xpath"])
            check_box[index].click()
            self.browser.find_element(*AdminPageLocators.COPY_BUTTON["xpath"]).click()
            success_text = self.browser.find_element(*AdminPageLocators.SUCCESS["xpath"]).text
            assert success_text == "Success: You have modified products!", "User doesn`t copy product"
        else:
            print("Don`t do it!!! Out of range")



