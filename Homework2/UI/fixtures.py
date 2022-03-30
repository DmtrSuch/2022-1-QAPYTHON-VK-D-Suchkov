import os
import shutil
import sys

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from UI.pages.login_page import LoginPage




def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture()
def driver(config, temp_dir):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": temp_dir})
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '98.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()

@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, temp_dir):
    failed_test_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_test_count:
        browser_logs = os.path.join(temp_dir, 'browser.log')
        with open(browser_logs, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
        screenshot_path = os.path.join(temp_dir, 'failed.png')
        allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
        with open(browser_logs, 'r') as f:
            allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)

@pytest.fixture(scope='session')
def credentials():
    with open('creds', 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'])
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()
    return cookies




