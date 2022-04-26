import os
import shutil

import allure
import pytest
from appium import webdriver
from selenium import webdriver as wd
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.menu_page import MenuPage

from ui import pages

from webdriver_manager.chrome import ChromeDriverManager
from ui.capability import capability_select


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page(config['device_os'], 'MainPage')
    return page(driver=driver, config=config)

@pytest.fixture
def menu_page(driver, config):
    page = get_page(config['device_os'], 'MenuPage')
    return page(driver=driver, config=config)



def get_page(device, page_class):
    if device == 'android':
        page_class += 'ANDROID'
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(device_os,  appium_url):
    if device_os == 'android':
        desired_caps = capability_select(device_os)
        driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
        return driver
    else:
        raise UnsupportedBrowserType(f' Unsupported device_os type {device_os}')


@pytest.fixture(scope='function')
def driver(config, test_dir):
    device_os = config['device_os']
    appium_url = config['appium']
    browser = get_driver(device_os,  appium_url)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir, config):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)
