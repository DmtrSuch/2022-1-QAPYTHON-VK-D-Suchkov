from UI.locators import basic_locators
from UI.pages.base_page import BasePage
import allure

class SegmentPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'
    locators = basic_locators.SegmentsPageLocator()

    @allure.step("Создаем cегмент")
    def CreateSegment(self,name):
        self.clickretry(SegmentPage.locators.CREATE_LOCATOR)
        self.clickretry(SegmentPage.locators.CID_LOCATOR)
        self.click(SegmentPage.locators.CHECK_BOX_LOCATOR)
        self.click(SegmentPage.locators.CREATE_LOCATOR)
        self.find(SegmentPage.locators.NAME_SEGMENT).clear()
        self.input(SegmentPage.locators.NAME_SEGMENT)
        self.click(SegmentPage.locators.CREATE_LOCATOR)