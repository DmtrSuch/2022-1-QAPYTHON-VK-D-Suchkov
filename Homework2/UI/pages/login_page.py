import allure
from UI.locators import basic_locators
from UI.pages.base_page import BasePage
from UI.pages.main_page import MainPage


class LoginPage(BasePage):

    url = 'https://target.my.com/'
    locators = basic_locators.LoginPageLocators()
    Timeout = 15

    @allure.step("Авторизовываемся")
    def login(self,user,password):
        self.click(LoginPage.locators.LOGIN_BUTTON_LOCATOR)
        self.input(LoginPage.locators.EMAIL_LOCATOR, user)
        self.input(LoginPage.locators.PASSWORD_LOCATOR, password)
        self.click(LoginPage.locators.ENTER_BUTTON_LOCATOR)
        return MainPage(self.driver)

