import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import time


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome", help='Choose browser: Chrome, Firefox, Edge')


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser")
    url = "http://192.168.218.128/opencart/upload/"
    # options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    if browser_name == "Chrome":
        # optionsChrome = ChromiumOptions()
        # optionsChrome.add_argument("--headless")
        # browser = webdriver.Chrome(options=optionsChrome)
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(10)
        browser.implicitly_wait(10)
        # browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Firefox":
        # optionsFF = FirefoxOptions()
        # optionsFF.headless = True
        # browser = webdriver.Firefox(options=optionsFF)
        browser = webdriver.Firefox()
        browser.implicitly_wait(10)
        browser.get(url)
        # browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Edge":
        # optionsEdge = EdgeOptions()
        # optionsEdge.add_argument("--headless")
        # browser = webdriver.Edge(options=optionsEdge)
        browser = webdriver.Edge()
        browser.implicitly_wait(10)
        browser.get(url)
        # browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
