from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGO = {"id": (By.ID, "logo"),
            "xpath" : (By.XPATH, "//div[@id='logo']/a/img")}
    CURRENCY = {"class_name": (By.CLASS_NAME, "fa-caret-down"),
                "xpath" : (By.XPATH, "//span[text()='Currency']") }
    CUR_LIST = { "class_name" : (By.CSS_SELECTOR, "#form-currency > div > ul"),
                 "xpath" : (By.XPATH, "//ul[@class='dropdown-menu show']")}
    TOP_LINKS = {"id" : (By.ID, "top"),
                 "xpath" : (By.XPATH, "//nav[@id='top']")}
    SEARCH_INPUT = {"name" : (By.NAME, "search"),
                    "xpath" : (By.XPATH, "//input[@name='search']")}
    SEARCH_BUTTON = {"class_name" : (By.CLASS_NAME, "fas fa-search"),
                     "xpath" : (By.XPATH, "//button[@class='btn btn-light btn-lg']")}
    NAV_BAR = {"css" : (By.CSS_SELECTOR, "ul.nav > li"),
               "xpath" : (By.XPATH, "//nav[@id='menu']")}
    FOOTER = {"tag" : (By.TAG_NAME, "footer"),
              "xpath" : (By.XPATH, "//footer")}
    CART = {"id" : (By.ID, "cart"),
            "xpath" : (By.XPATH, "//div[@id='header-cart']")}
    PRODUCT = {"class_name" : (By.CLASS_NAME, "product-thumb"),
               "xpath" : (By.XPATH, "//div[@class='product-thumb']")}
    SWIPER_NEXT = {"class_name" : (By.CLASS_NAME, "swiper-button-next"),
                   "xpath" : (By.XPATH, "//button[@class='carousel-control-next']")}
    SWIPER_PREV = {"class_name" : (By.CLASS_NAME, "swiper-button-prev"),
                   "xpath": (By.XPATH, "//button[@class='carousel-control-prev']")}
    ADD_TO_CART = {"class_name" : (By.CLASS_NAME, "fa-shopping-cart"),
                   "xpath": (By.XPATH, "//button[contains(@aria-label, 'Add to Cart')]") }
    SUCCESS_TEXT = {"class_name" : (By.CLASS_NAME, "fas fa-exclamation-circle"),
                    "xpath" : (By.XPATH, "//i[@class='fas fa-exclamation-circle']")}
    SEARCH_ERROR = {"tag" : (By.TAG_NAME, "h5"),
                    "xpath" : (By.XPATH, "//h5")}
    PRODUCT_NAME = {"tag" : (By.TAG_NAME, "h4"),
                    "xpath" : (By.XPATH, "//h4")}