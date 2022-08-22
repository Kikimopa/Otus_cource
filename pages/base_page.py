from selenium.common.exceptions import NoSuchElementException



class BasePage():
    def __init__(self, browser):
        self.browser = browser
        # self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

    def open_admin_page(self):
        self.browser.get(self.url + "admin")
