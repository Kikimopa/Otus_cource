import time

from .pages.locators import DragNDropLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_basic(browser_d_n_d):
    actions = ActionChains(browser_d_n_d)
    url = "https://marcojakob.github.io/dart-dnd/basic/"
    browser_d_n_d.get(url)
    trash = browser_d_n_d.find_element(*DragNDropLocators.TRASH)
    for items in range(5):
        file = browser_d_n_d.find_element(*DragNDropLocators.FILE)
        actions.drag_and_drop(file, trash).perform()

def test_Custom_Drag_Avatar(browser_d_n_d):
    actions = ActionChains(browser_d_n_d)
    url = "https://marcojakob.github.io/dart-dnd/custom_avatar/"
    browser_d_n_d.get(url)
    trash = browser_d_n_d.find_element(*DragNDropLocators.TRASH)
    for items in range(5):
        file = browser_d_n_d.find_element(*DragNDropLocators.FILE)
        actions.drag_and_drop(file, trash).perform()

def test_Drag_Detection_Only(browser_d_n_d):
    actions = ActionChains(browser_d_n_d)
    url = "https://marcojakob.github.io/dart-dnd/detection_only/"
    browser_d_n_d.get(url)
    point = browser_d_n_d.find_element(*DragNDropLocators.POINT)
    actions.click_and_hold(point).move_by_offset(100, 200).perform()
    print(point.text)

def test_Free_Dragging(browser_d_n_d):
    actions = ActionChains(browser_d_n_d)
    url = "https://marcojakob.github.io/dart-dnd/free_dragging/"
    browser_d_n_d.get(url)
    point = browser_d_n_d.find_element(*DragNDropLocators.POINT)
    actions.click_and_hold(point).move_by_offset(450, 389).perform()


