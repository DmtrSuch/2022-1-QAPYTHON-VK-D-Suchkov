from UI.locators import basic_locators
from UI.pages.base_page import BasePage
import allure

class CompanyPage(BasePage):
    url = 'https://target.my.com/campaign/new'
    locators = basic_locators.CompanyPageLocator()
    intro = ''

    @allure.step("Создаем компанию")
    def CreateCompany(self,name,file_path):
        self.clickretry(CompanyPage.locators.TRAFFIC_LOCATOR)
        self.input(CompanyPage.locators.REFERENCE_LOCATOR,'https://'+name+'.com')
        self.clickretry(CompanyPage.locators.NAME_COMPANY_LOCATOR)
        self.find(CompanyPage.locators.NAME_COMPANY_LOCATOR).clear()
        self.input(CompanyPage.locators.NAME_COMPANY_LOCATOR,name)
        self.scroll(CompanyPage.locators.BANNER_COMPANY_LOCATOR)
        self.click(CompanyPage.locators.BANNER_COMPANY_LOCATOR)
        self.clickretry(CompanyPage.locators.BANNERS_CMP_LOCATOR)
        self.upload(CompanyPage.locators.ROLES_LOCATOR,file_path)
        self.clickretry(CompanyPage.locators.SAVE_COMPANY_LOCATOR)

