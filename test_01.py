import pytest
from selenium.webdriver.common.by import By

url = "http://192.168.218.128/opencart/upload/"

def test_01(browser):
    browser.get(url)
    h1 = browser.find_element(By.TAG_NAME, "h1").text
    assert h1 == "Your Store", 'It is not opencart homepage'



if __name__ == "__main__":
    pytest.main()