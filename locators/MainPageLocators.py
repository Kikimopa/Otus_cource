from selenium.webdriver.common.by import By

class MainPageLocators:

    TOP_LINKS = (By.ID, "top-links")
    SEARCH_INPUT = (By.NAME, "search")
    NAV_BAR = (By.CLASS_NAME, "nav navbar-nav")
    FOOTER = (By.TAG_NAME, "footer")
    CART = (By.ID, "cart")
    PRODUCT = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/h4/a')
    SWIPER_NEXT = (By.CLASS_NAME, "swiper-button-next")
    SWIPER_PREV = (By.CLASS_NAME, "swiper-button-prev")


