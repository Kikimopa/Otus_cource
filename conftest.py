import datetime
import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromiumOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

def pytest_addoption(parser):
    parser.addoption('--browser', "-B", action='store', default="Chrome", help='Choose browser: Chrome, Firefox, Edge')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    # url = "https://demo.opencart.com/"
    if browser_name == "Chrome":
        options = ChromiumOptions()
        options.add_argument("--headless")
        #browser = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
        browser = EventFiringWebDriver(webdriver.Chrome(), MyListener())
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Firefox":
        browser = EventFiringWebDriver(webdriver.Firefox(), MyListener())
        yield browser
        print("\nquit browser..")
        browser.close()
    elif browser_name == "Edge":
        browser = EventFiringWebDriver(webdriver.Edge(), MyListener())
        yield browser
        print("\nquit browser..")
        browser.close()
    else:
        raise Exception(f"{request.param} is not supported!")



class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        print(f"\nHey Bro, I`m get ready to find element: {by}:{value}")

    def after_find(self, by, value, driver):
        print(f"Bro, I`m find an element: {by}:{value}")

    def before_click(self, element, driver):
        print(f"Hey Bro, I want click to element")

    def after_click(self, element, driver):
        print(f"Bro, I clicked to element")

    def before_close(self, driver):
        print(f"Hey Bro, I want to close browser")

    def after_close(self, driver):
        print(f"Bro, I closed browser")

    def before_quit(self, driver):
        print(f"Hey Bro, I want to quit from browser")

    def after_quit(self, driver):
        print(f"Bro, I was quit from browser")

    def on_exception(self, exception, driver):
        print(f"Something happened. I`m taking screenshot")
        driver.get_screenshot_as_file(rf"screenshots\{datetime.datetime.now()}.png")





@pytest.fixture(scope="function")
def browser_d_n_d():
    browser = webdriver.Chrome()
    yield browser
    browser.close()