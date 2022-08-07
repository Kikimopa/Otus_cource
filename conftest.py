import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome", help='Choose browser: Chrome, Firefox, Edge')


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser")

    # options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    if browser_name == "Chrome":
        optionsChrome = ChromiumOptions()
        optionsChrome.add_argument("--headless")
        browser = webdriver.Chrome(options=optionsChrome)
        browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Firefox":
        optionsFF = FirefoxOptions()
        optionsFF.headless = True
        browser = webdriver.Firefox(options=optionsFF)
        browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Edge":
        optionsEdge = EdgeOptions()
        optionsEdge.add_argument("--headless")
        browser = webdriver.Edge(options=optionsEdge)
        browser.maximize_window()
        yield browser
        print("\nquit browser..")
        browser.close()
