from selenium.webdriver.common.by import By

class AdminPageLocators:
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    SUBMIT =(By.TAG_NAME, "button")
    BUTTON_CLOSE_ALERT = {"id" : (By.ID, "container"),
                          "xpath" : (By.XPATH, "//button[@class='btn-close']")}
    DASHBORD = (By.TAG_NAME, "h1")
    MENU = (By.ID, "menu")
    USER_DROPDOWN = (By.CLASS_NAME, "dropdown")
    TILE_FOTTER = (By.CLASS_NAME, "tile-footer")
    WORLD_MAP_PLUS = (By.CLASS_NAME, "jqvmap-zoomin")
    WORLD_MAP_MINUS = (By.CLASS_NAME, "jqvmap-zoomout")
    LOGO = (By.ID, "header")
    COLOMN_LEFT = (By.ID, "column-left")
    CATALOG = {"class_name" : (By.CLASS_NAME, "parent collapsed"),
               "xpath" : (By.XPATH, "//ul[@id='menu']/li[2]")}
    PRODUCTS = {"css" : (By.CSS_SELECTOR, "#menu ul li"),
                "xpath" : (By.XPATH, "//ul[@id='menu']/li[2]/ul/li[2]")}
    PRODUCT_TITLE = {"tag" : (By.TAG_NAME, "h1"),
                     "xpath" : (By.XPATH, "//h1")}
    ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a > i")
    ADD_PRODUCT_TITLE = (By.CLASS_NAME, "card-header")
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
    DOWNLOAD_AREA = (By.NAME, "file")
    DOWNLOAD_NAME = (By.CSS_SELECTOR, '#form-download > div:nth-child(1) > div > div > input')
    DOWNLOAD_FILE_NAME = (By.NAME, "filename")
    DOWNLOAD_MASK = (By.ID, "input-mask")
    BUTTONS = (By.CLASS_NAME, "pull-right")
    ADD_DOWNLOAD_BUTTON = (By.TAG_NAME, "a")
    SAVE_DOWNLOAD_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button/i')
    ATTANTION = (By.CLASS_NAME, "text-danger")