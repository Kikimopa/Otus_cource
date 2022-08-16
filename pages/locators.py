from selenium.webdriver.common.by import By

class MainPageLocators:

    TOP_LINKS = (By.ID, "top-links")
    SEARCH_INPUT = (By.NAME, "search")
    NAV_BAR = (By.CSS_SELECTOR, "ul.nav > li")
    FOOTER = (By.TAG_NAME, "footer")
    CART = (By.ID, "cart")
    PRODUCT = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/h4/a')
    SWIPER_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SWIPER_PREV = (By.CLASS_NAME, "swiper-button-prev")

class AdminPageLocators:
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT =(By.TAG_NAME, "button")
    MENU = (By.ID, "menu")
    USER_DROPDOWN = (By.CLASS_NAME, "dropdown")
    TILE_FOTTER = (By.CLASS_NAME, "tile-footer")
    WORLD_MAP_PLUS = (By.CLASS_NAME, "jqvmap-zoomin")
    WORLD_MAP_MINUS = (By.CLASS_NAME, "jqvmap-zoomout")
    LOGO = (By.ID, "header-logo")
    COLOMN_LEFT = (By.ID, "column-left")
    CATALOG = (By.CLASS_NAME, "parent collapsed")
    PRODUCTS = (By.CSS_SELECTOR, "#menu ul li")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    ADD_PRODUCT = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    ADD_PRODUCT_TITLE = (By.CLASS_NAME, "panel-title")
    INPUT_PRODUCT_NAME = (By.ID, "input-name1")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "panel-body")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    NAV_MENU = (By.CSS_SELECTOR, "ul.nav > li")
    MODEL = (By.NAME, "model")
    DATA = (By.XPATH, '//*[@id="form-product"]/ul/li[2]')
    SAVE_BUTTON = (By.CLASS_NAME, "fa fa-save")
    SUCCESS = (By.CLASS_NAME, "alert alert-success alert-dismissible")
    CHECKBOX = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]")
    DELETE_BUTTON = (By.CLASS_NAME, "fa-trash-o")

class ItemCardLocators:
    ITEM_IMGS = (By.CLASS_NAME, "thumbnails")
    ITEM_NAV = (By.CLASS_NAME, "nav nav-tabs")
    BUTTONS = (By.CLASS_NAME, "btn-group")
    QUANTITY = (By.NAME, "quantity")
    ADD_TO_CART = (By.ID, "button-cart")

class DragNDropLocators:
    BASIC = (By.ID, "custom-drag-avatar")
    FILE = (By.CLASS_NAME, "document")
    TRASH = (By.CSS_SELECTOR, "body > div > div")
    POINT = (By.CLASS_NAME, "draggable")