from UI.locators import basic_locators
from UI.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import allure

class SegmentPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'
    locators = basic_locators.SegmentsPageLocator()

    @allure.step("Создаем cегмент")
    def CreateSegment(self,name):
        try:
            self.clickretry(SegmentPage.locators.CREATE_LOCATOR)
        except TimeoutException:
            self.clickretry(SegmentPage.locators.FIRST_CREATE_LOCATOR)
        self.clickretry(SegmentPage.locators.CH_LOCATOR)
        self.clickretry(SegmentPage.locators.ADDING_SEGMENT_SOURCE)
        self.clickretry(SegmentPage.locators.VALUE_PAY_SOURCE_LOCATOR)
        self.clickretry(SegmentPage.locators.ADD_LOCATOR)
        self.find(SegmentPage.locators.INPUT_LOCATOR).clear()
        self.input(SegmentPage.locators.INPUT_LOCATOR,name)
        self.clickretry(SegmentPage.locators.CREATE_SEGMENT_LOCATOR)
