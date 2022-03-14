from selenium.webdriver.remote.webelement import WebElement
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage(object):
    locators = BasePageLocators()
    CLICK_RETRY = 10

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def input(self, locator, query):
        elem = self.find(locator)
        elem.send_keys(query)

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

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

    def login(self):
        self.click(BasePage.locators.LOGIN_BUTTON_LOCATOR)
        self.input(BasePage.locators.EMAIL_LOCATOR, self.config['login'])
        self.input(BasePage.locators.PASSWORD_LOCATOR, self.config['password'])
        self.click(BasePage.locators.ENTER_BUTTON_LOCATOR)


class MainPage(BasePage):
    locators = MainPageLocators()

    def logout(self):
        for i in range(MainPage.CLICK_RETRY):
            try:
                self.click(MainPage.locators.SCROLL_MENU_LOCATOR)
                self.click(MainPage.locators.LOGOUT_BUTTON_LOCATOR)
                return
            except ElementClickInterceptedException:
                if i == MainPage.CLICK_RETRY - 1:
                    raise
            except StaleElementReferenceException:
                if i == MainPage.CLICK_RETRY - 1:
                    raise


class ProfilePage(MainPage):
    locators = ProfilePageLocators()

    def changerandominfo(self):
        self.clickretry(ProfilePage.locators.PROFILE_LOCATOR)
        self.clickretry(ProfilePage.locators.FULLNAME_INFO_LOCATOR)
        self.find(ProfilePage.locators.FULLNAME_INFO_LOCATOR).clear()
        self.find(ProfilePage.locators.NUMBER_INFO_LOCATOR).clear()
        self.input(ProfilePage.locators.FULLNAME_INFO_LOCATOR, self.config['fullname'])
        self.input(ProfilePage.locators.NUMBER_INFO_LOCATOR, self.config['number'])
        self.click(ProfilePage.locators.SAVE_INFO_LOCATOR)


class BillingPage(MainPage):
    locators = BillingPageLocators()


class ToolsPage(MainPage):
    locators = ToolsPageLocators()
