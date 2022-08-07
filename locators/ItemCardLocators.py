from selenium.webdriver.common.by import By

class ItemCardLocators:
    ITEM_IMGS = (By.CLASS_NAME, "thumbnails")
    ITEM_NAV = (By.CLASS_NAME, "nav nav-tabs")
    BUTTONS = (By.CLASS_NAME, "btn-group")
    QUANTITY = (By.NAME, "quantity")
    ADD_TO_CART = (By.ID, "button-cart")
    
