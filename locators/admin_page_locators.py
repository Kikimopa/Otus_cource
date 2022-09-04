from selenium.webdriver.common.by import By

class AdminPageLocators:
    LOGIN = {"name" : (By.NAME, "username"),
             }
    PASSWORD = {"name" : (By.NAME, "password"),
                }
    SUBMIT = {"tag" : (By.TAG_NAME, "button"),
              }
    BUTTON_CLOSE_ALERT = {"id" : (By.ID, "container"),
                          "xpath" : (By.XPATH, "//div[@class='modal-header']/button")}
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
    ADD_PRODUCT = {"css" : (By.CSS_SELECTOR, "#content > div.page-header > div > div > a > i"),
                   "xpath_demo" : (By.XPATH, "//button[@aria-label='Filter']"),
                   "xpath_my" : (By.XPATH, "//i[@class='fa fa-plus']")}
    ADD_PRODUCT_TITLE = {"class_name" : (By.CLASS_NAME, "card-header"),
                         "xpath_demo" : (By.XPATH, "//div[@class='card-header']"),
                         "xpath_my" : (By.XPATH, "//h3[@class='panel-title']")}
    INPUT_PRODUCT_NAME = {"id" : (By.ID, "input-name1"),
                          "xpath" : (By.XPATH, "//input[@id='input-name1']")}
    PRODUCT_DESCRIPTION = {"class_name" : (By.CLASS_NAME, "panel-body"),
                           "xpath_demo": (By.XPATH, "//iframe"),
                           "xpath_my" : (By.XPATH, "//div[@class='note-editable panel-body']/p")}
    META_TAG_TITLE = {"id" : (By.ID, "input-meta-title1"),
                      "xpath": (By.XPATH, "//input[@id='input-meta-title1']")}
    NAV_MENU = {"css" : (By.CSS_SELECTOR, "ul.nav > li"),
                "xpath": (By.XPATH, "//ul[@class='nav nav-tabs']")}
    MODEL = {"name" : (By.NAME, "model"),
             "xpath": (By.XPATH, "//input[@id='input-model']")}
    DATA = {"xpath" : (By.XPATH, "//ul[@class='nav nav-tabs']/li[2]")}
    SAVE_BUTTON = {"class_name" : (By.CLASS_NAME, "fa fa-save"),
                   "xpath": (By.XPATH, "//button[@aria-label='Save']")}
    SUCCESS = {"class_name" : (By.CLASS_NAME, "alert alert-success alert-dismissible"),
               "xpath": (By.XPATH, "//i[@class='fa fa-check-circle']")}
    CHECKBOX = {"css" : (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]"),
                "xpath": (By.XPATH, "//tbody/tr/td/input")}
    DELETE_BUTTON = {"class_name" : (By.CLASS_NAME, "fa-trash-o"),
                     "xpath": (By.XPATH, "//i[@class='fa fa-trash-o']")}
    DOWNLOADS = {"xpath": (By.XPATH, "//ul[@id='menu']/li[2]/ul/li[8]")}
    DOWNLOAD_AREA = {"class_name" : (By.NAME, "file"),
                     "xpath" : (By.XPATH, "")}
    DOWNLOAD_NAME = {"css" : (By.CSS_SELECTOR, '#form-download > div:nth-child(1) > div > div > input'),
                     "xpath" : (By.XPATH, "")}
    DOWNLOAD_FILE_NAME = {"name" : (By.NAME, "filename") ,
                          "xpath" : (By.XPATH, "")}
    DOWNLOAD_MASK = {"id" : (By.ID, "input-mask"),
                     "xpath" : (By.XPATH, "")}
    BUTTONS = {"class_name" : (By.CLASS_NAME, "pull-right"),
               "xpath" : (By.XPATH, "")}
    ADD_DOWNLOAD_BUTTON = {"tag" : (By.TAG_NAME, "a"),
                           "xpath" : (By.XPATH, "")}
    ATTANTION = {"class_name" : (By.CLASS_NAME, "text-danger"),
                 "xpath" : (By.XPATH, "")}
    COPY_BUTTON = {"xpath" : (By.XPATH, "//i[@class='fa fa-copy']")}