from selenium.webdriver.common.by import By


class ProductPageLocators:
    ITEM_IMGS = (By.CLASS_NAME, "col-sm")
    ITEM_NAV = (By.CLASS_NAME, "nav nav-tabs")
    BUTTONS = (By.CLASS_NAME, "btn-group")
    QUANTITY = (By.NAME, "quantity")
    ADD_TO_CART = (By.ID, "button-cart")
    SCROLL_IMG = (By.XPATH, "/html/body/div[2]/div/button[2]")
    COUNT_IMGS = (By.TAG_NAME, "a")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    IMG_NAME = (By.CLASS_NAME, "mfp-title")
    LIKE = (By.CLASS_NAME, "fa-heart")
    COMPARE = (By.CLASS_NAME, "fa-exchange-alt")
    H2 = (By.TAG_NAME, "h2")
    SHOPPING_CART = (By.CLASS_NAME, "fa-shopping-cart")
