import os

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from code.config.creds import APP_PORT, APP_SERVICE, APP_HOST
from code.ui.pages.Login_page import LoginPage
from code.ui.pages.Main_page import MainPage
from code.ui.pages.Register_page import RegPage

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome')
    parser.addoption('--url', default=f'http://{APP_SERVICE}:{APP_PORT}/login')
    parser.addoption("--selenoid", action="store_true")
    parser.addoption("--vnc", action="store_true")

@pytest.fixture(scope="session")
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))

@pytest.fixture(scope="function", autouse=True)
def log_in(browser, request):
    if 'reg' in request.keywords:
        login_url = f"http://{APP_SERVICE}:{APP_PORT}/login"
        page = LoginPage(browser, login_url)
        page.browser.get(page.url)
        browser.maximize_window()
        page.go_to_register_page()
        return RegPage(browser, browser.current_url)
    if 'noautologin' in request.keywords:
        return
    LOGIN = "Adminadmin"
    PASSWORD = "Adminadmin"
    login_url = f"http://{APP_SERVICE}:{APP_PORT}/login"
    page = LoginPage(browser, login_url)
    page.browser.get(page.url)
    browser.maximize_window()
    page.login(LOGIN, PASSWORD)
    return MainPage(browser, browser.current_url)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser_name')
    return {'url': url, 'browser': browser}


def get_driver(config):
    browser_name = config['browser']
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.set_capability("browserVersion", "100.0")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        caps = {'browserName': browser_name,
                'version': '100.0'
                }
        browser = webdriver.Remote(command_executor=f"http://selenoid:4444/wd/hub",
                                   options=options, desired_capabilities=caps)

    else:
        raise KeyError
    return browser


@pytest.fixture(scope='function')
def browser(config):
    url = config['url']
    browser = get_driver(config)
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/login"
    page = LoginPage(browser, url)
    page.browser.get(page.url)
    browser.maximize_window()
    return page


@pytest.fixture(scope="function")
def main_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
    page = MainPage(browser, url)
    page.browser.get(page.url)
    browser.maximize_window()
    return page


@pytest.fixture(scope="function")
def register_page(browser):
    url = f"http://{APP_SERVICE}:{APP_PORT}/reg"
    page = RegPage(browser, url)
    page.browser.get(page.url)
    browser.maximize_window()
    return page