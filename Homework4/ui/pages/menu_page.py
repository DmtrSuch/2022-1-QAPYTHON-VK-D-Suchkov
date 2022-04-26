from ui.pages.base_page import BasePage
from ui.pages.base_page import PageNotLoadedException
from ui.locators.locators_android import MenuPageANDROIDLocators
import allure




class MenuPage(BasePage):
    locators = MenuPageANDROIDLocators()
    def changenews(self):
        pass

    def exit(self):
        pass

    def checkversion(self):
        pass


class MenuPageANDROID(MenuPage):
    locators = MenuPageANDROIDLocators()

    @allure.step("Меняем источник новостей")
    def changenews(self):
        self.swipe_to_element(self.locators.SOURCE_NEWS_LOCATOR,1)
        self.click_for_android(self.locators.SOURCE_NEWS_LOCATOR)
        self.click_for_android(self.locators.MAIL_NEWS_LOCATOR)
        self.click_for_android(self.locators.CHECK_MARK)
        self.click_for_android(self.locators.BACK_NEWS_LOCATOR)

    def exit(self):
        self.click_for_android(self.locators.EXIT_MENU_LOCATOR)

    def checkversion(self):
        self.swipe_to_element(self.locators.CHECK_VERSION_LOCATOR, 1)
        self.click_for_android(self.locators.CHECK_VERSION_LOCATOR)
