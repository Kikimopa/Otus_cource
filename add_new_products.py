import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

url = "http://192.168.218.128/opencart/upload/admin/"
# url = "http://192.168.218.128/opencart/upload/"
product_url = "http://192.168.218.128/opencart/upload/admin/index.php?route=catalog/product&user_token=SNbLHHu2JlyDgfl0Qpgb3BdoiK6cbUSV"

browser = webdriver.Chrome()
browser.get(product_url)


browser.find_element(By.NAME, "username").send_keys("admin")
browser.find_element(By.NAME, "password").send_keys("admin")
browser.find_element(By.TAG_NAME, "button").click()


wb = openpyxl.load_workbook("phones.xlsx")
sheet = wb.active
for items in sheet.rows:
    item_model = items[0]
    item_name = items[1]
    item_price = items[2]
    item_desc = items[3]
    item_type = items[4]
    item_color = items[5]


# """Add new product"""
    browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > a").click()
    name = browser.find_element(By.CSS_SELECTOR, "#input-name1")
    name.send_keys(str(item_name.value))
    desc = browser.find_element(By.CSS_SELECTOR, "#language1 > div:nth-child(2) > div > div > div.note-editing-area > div.note-editable.panel-body")
    desc.send_keys(str(item_desc.value))
    meta_tags = browser.find_element(By.CSS_SELECTOR, "#input-meta-title1")
    meta_tags.send_keys(str(item_type.value))
    browser.find_element(By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a").click()
    model = browser.find_element(By.CSS_SELECTOR, "#input-model")
    model.send_keys(str(item_model.value))
    price = browser.find_element(By.CSS_SELECTOR, "#input-price")
    price.send_keys(str(item_price.value))
    browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button").click()



time.sleep(2)

browser.close()
browser.quit()