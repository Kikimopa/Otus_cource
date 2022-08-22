from selenium.webdriver.common.by import By

class DragNDropLocators:
    BASIC = (By.ID, "custom-drag-avatar")
    FILE = (By.CLASS_NAME, "document")
    TRASH = (By.CSS_SELECTOR, "body > div > div")
    POINT = (By.CLASS_NAME, "draggable")