import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from UI.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import os


class PageNotOpenedException(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://target.my.com/'
    CLICK_RETRY = 15
    Timeout = 3

    def __init__(self, driver):
        self.driver = driver
        self.is_opened(self.Timeout)

    def is_opened(self, timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(
            f'{self.url} did not opened in {timeout} for {self.__class__.__name__}.Current url: {self.driver.current_url}.')


    @allure.step('Find element')
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Find element')
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Input')
    def input(self, locator, query):
        elem = self.find(locator)
        elem.send_keys(query)

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('Try click element')
    def clickretry(self, locator):
        for i in range(BasePage.CLICK_RETRY):
            try:
                self.click(locator)
                return
            except ElementClickInterceptedException:
                if i == BasePage.CLICK_RETRY - 1:
                    raise
            except StaleElementReferenceException:
                if i == BasePage.CLICK_RETRY - 1:
                    raise

    @allure.step('Try use scroll menu')
    def scrollclickretry(self,LCTRButton1,LCTRButton2):
        for i in range(BasePage.CLICK_RETRY):
            try:
                self.click(LCTRButton1)
                self.click(LCTRButton2)
                return
            except ElementClickInterceptedException:
                if i == BasePage.CLICK_RETRY - 1:
                    raise
            except StaleElementReferenceException:
                if i == BasePage.CLICK_RETRY - 1:
                    raise

    @allure.step('Scroll')
    def scroll(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find(element)).perform()



    @allure.step('Upload')
    def upload(self,locator,file_path):
        elem = self.find(locator)
        elem.send_keys(file_path)