from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class BasePage():
    def __init__(self, browser):
        self.browser = browser
        # self.url = url

    # def open(self):
    #     self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

    def go_to_admin_page(self):
        self.browser.get("http://192.168.218.128/opencart/upload/admin")

    def go_to_main_page(self):
        self.browser.get("http://192.168.218.128/opencart/upload")


