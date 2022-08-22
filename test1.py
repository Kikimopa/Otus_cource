import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://demo.opencart.com/"

browser = webdriver.Chrome()
browser.get(url)

location = browser.find_element(By.CLASS_NAME, "fa-caret-down").click()
location2 = browser.find_element(By.CLASS_NAME, "dropdown-menu show")
assert location2 , "No"




browser.close()