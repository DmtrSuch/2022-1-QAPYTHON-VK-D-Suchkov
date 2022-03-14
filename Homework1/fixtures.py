import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages import *


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver, config=config)


@pytest.fixture
def profile_page(driver, config):
    return ProfilePage(driver=driver, config=config)


@pytest.fixture
def tools_page(driver, config):
    return ToolsPage(driver=driver, config=config)


@pytest.fixture
def billing_page(driver, config):
    return BillingPage(driver=driver, config=config)
