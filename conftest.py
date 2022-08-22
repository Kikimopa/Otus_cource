import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

#http://192.168.218.128/opencart/upload/admin/

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome", help='Choose browser: Chrome, Firefox, Edge')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    url = "https://demo.opencart.com/"
    if browser_name == "Chrome":
        browser = webdriver.Chrome()
        browser.get(url)
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Firefox":
        browser = webdriver.Firefox()
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Edge":
        browser = webdriver.Edge()
        yield browser
        print("\nquit browser..")
        browser.close()

# @pytest.fixture(scope="function")
# def browser_adminPage(request):
#     browser_name = request.config.getoption("browser")
#     # url = "http://192.168.218.128/opencart/upload/admin"
#     browser = webdriver.Chrome()
#     # browser.get(url)
#     yield browser
#     browser.close()
#
@pytest.fixture(scope="function")
def browser_d_n_d(request):
    browser = webdriver.Chrome()
    yield browser
    browser.close()