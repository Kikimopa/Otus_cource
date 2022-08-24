import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://192.168.218.128/opencart/upload/admin"

browser = webdriver.Chrome()
browser.get(url)
browser.get("http://192.168.218.128/opencart/upload/admin/index.php?route=catalog/download&user_token=9iVLs1Z765I0QOKFupMFoz34st0m3yzw")
browser.find_element(By.NAME, "username").send_keys("admin")
browser.find_element(By.NAME, "password").send_keys("admin")
browser.find_element(By.TAG_NAME, "button").click()


buttons = browser.find_elements(By.CLASS_NAME,"pull-right")[-1]
buttons.find_elements(By.TAG_NAME, "a")[0].click()


save = browser.find_elements(By.CLASS_NAME, "btn btn-primary")

print(len(save))

time.sleep(3)




browser.close()