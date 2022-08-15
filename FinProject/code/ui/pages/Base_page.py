import allure
from selenium.webdriver import ActionChains

from code.utils.decorators import wait

from code.mock_api.api_vk_client import VkApiClient

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, \
    TimeoutException, WebDriverException


TIME_TO_WAIT = 10


class PageNotLoadedException(Exception):
    pass


class BasePage(object):

    locators = None

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.API = VkApiClient()
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.browser.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {TIME_TO_WAIT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.browser.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=TIME_TO_WAIT, interval=0.1)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def scroll_to(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true)", element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = TIME_TO_WAIT
        return WebDriverWait(self.browser, timeout=timeout)

    @allure.step("Clicking {locator}")
    def click(self, locator, timeout=None):
        def _click():
            element = self.find(locator, timeout=timeout)
            self.scroll_to(element)
            element.click()
            return True

        return wait(_click, error=ElementNotInteractableException, check=True, timeout=timeout)

    @allure.step("Writing {locator}")
    def write(self, words, locator, timeout=None):
        def _write():
            line = self.find(locator, timeout=timeout)
            self.scroll_to(line)
            line.clear()
            line.send_keys(words)
            return True

        return wait(_write, error=StaleElementReferenceException, check=True, timeout=timeout, interval=0.1)

    @allure.step("Go to element {locator}")
    def move_to_element(self, locator):
        item = self.find(locator)
        ActionChains(self.browser).move_to_element(item).perform()

    @allure.step("Check El {locator} is not present")
    def not_element_present(self, locator, timeout=TIME_TO_WAIT):
        try:
            self.find(locator, timeout)
        except TimeoutException:
            return True
        return False

    @allure.step("Check text of {locator}")
    def text_present(self, locator, text, timeout=TIME_TO_WAIT):
        try:
            self.wait(timeout).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            return False
        return True

    @allure.step("Check El {locator} is present")
    def element_present(self, locator):
        try:
            self.find(locator)
        except WebDriverException:
            return False
        return True