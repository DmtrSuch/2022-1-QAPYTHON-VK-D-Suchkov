from UI.locators import basic_locators
from UI.pages.base_page import BasePage
from UI.pages.company_page import CompanyPage
from UI.pages.segments_page import SegmentPage
import allure




class MainPage(BasePage):
    url = 'https://target.my.com/dashboard'
    locators = basic_locators.MainPageLocators()

    @allure.step("Выходим")
    def logout(self):
        self.scrollclickretry(MainPage.locators.SCROLL_MENU_LOCATOR,MainPage.locators.LOGOUT_BUTTON_LOCATOR)
        return BasePage(self.driver)

    @allure.step("переход в раздел кмп")
    def Go_To_Create_Company(self):
        self.clickretry(MainPage.locators.CREATE_COMPANY_LOCATOR)
        return CompanyPage(self.driver)

    @allure.step("Раздел сегментов")
    def Go_To_Segmetns(self):
        self.clickretry(MainPage.locators.SEGMENT_LOCATOR)
        return SegmentPage(self.driver)