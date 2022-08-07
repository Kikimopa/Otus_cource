from selenium.webdriver.common.by import By

class AdminPageLocators:
    MENU = (By.ID, "menu")
    USER_DROPDOWN = (By.CLASS_NAME, "dropdown")
    TILE_FOTTER = (By.CLASS_NAME, "tile-footer")
    WORLD_MAP_PLUS = (By.CLASS_NAME, "jqvmap-zoomin")
    WORLD_MAP_MINUS = (By.CLASS_NAME, "jqvmap-zoomout")