from selenium.webdriver.common.by import By


class ProductPageLocators:
    ITEM_IMGS = {"class_name": (By.CLASS_NAME, "col-sm"),
                 "xpath": (By.XPATH, "//div[@class='image magnific-popup']")}
    NAV_TAB_ITEMS = {"class_name" : (By.CLASS_NAME, "nav nav-tabs"),
                "xpath" : (By.XPATH, "//ul[@class='nav nav-tabs']/li")}
    NAV_TAB = {"xpath" : (By.XPATH, "//ul[@class='nav nav-tabs']")}
    QUANTITY = {"name" : (By.NAME, "quantity"),
                "xpath": (By.XPATH, "//input[@name='quantity']")}
    ADD_TO_CART = {"id" : (By.ID, "button-cart"),
                   "xpath": (By.XPATH, "//button[@id='button-cart']")}
    SCROLL_IMG = {(By.XPATH, "/html/body/div[2]/div/button[2]")}
    SCROLL_IMG_NEXT = {"xpath" : (By.XPATH, "//button[contains(@title, 'Next')]")}
    SCROLL_IMG_PREV = {"xpath" : (By.XPATH, "//button[contains(@title, 'Previous')]")}
    COUNT_IMGS = {"tag" : (By.TAG_NAME, "a"),
                  "xpath" : (By.XPATH, "//div[@class='image magnific-popup']/div/a/img")}
    COUNT_IMGS_IN_HOLDER = {"tag" : (By.TAG_NAME, "a"),
                  "xpath": (By.XPATH, "//div[@class='mfp-counter']")}
    PRODUCT_NAME = {"tag": (By.TAG_NAME, "h1"),
                    "xpath": (By.XPATH, "//h1")}
    IMG_NAME = {"class_name" : (By.CLASS_NAME, "mfp-title"),
                "xpath": (By.XPATH, "//div[@class='mfp-title']")}
    LIKE = {"class_name" : (By.CLASS_NAME, "fa-heart"),
            "xpath": (By.XPATH, "//button/i[@class='fas fa-heart']")}
    COMPARE = {"class_name" : (By.CLASS_NAME, "fa-exchange-alt"),
               "xpath": (By.XPATH, "//button/i[@class='fas fa-exchange-alt']")}
    SUCCESS_TEXT = {"class_name": (By.CLASS_NAME, "fas fa-exclamation-circle"),
                    "xpath": (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")}