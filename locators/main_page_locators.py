from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGO = (By.ID, "logo")
    CURRENCY = (By.CLASS_NAME, "fa-caret-down")
    CUR_LIST = (By.CSS_SELECTOR, "#form-currency > div > ul")
    TOP_LINKS = (By.ID, "top-links")
    SEARCH_INPUT = (By.NAME, "search")
    NAV_BAR = (By.CSS_SELECTOR, "ul.nav > li")
    FOOTER = (By.TAG_NAME, "footer")
    CART = (By.ID, "cart")
    PRODUCT = (By.CLASS_NAME, "product-thumb")
    SWIPER_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SWIPER_PREV = (By.CLASS_NAME, "swiper-button-prev")
    ADD_TO_CART = (By.CLASS_NAME, "fa-shopping-cart")
    SUCCESS_TEXT = (By.CLASS_NAME, "fas fa-exclamation-circle")