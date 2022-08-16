import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://192.168.218.128/opencart/upload/admin/"
# url = "http://192.168.218.128/opencart/upload/"
product_url = "http://192.168.218.128/opencart/upload/admin/index.php?route=catalog/product&user_token=SNbLHHu2JlyDgfl0Qpgb3BdoiK6cbUSV"

browser = webdriver.Chrome()
browser.get(product_url)

browser.find_element(By.NAME, "username").send_keys("admin")
browser.find_element(By.NAME, "password").send_keys("admin")
browser.find_element(By.TAG_NAME, "button").click()

browser.find_element(By.CSS_SELECTOR, "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]").click()
