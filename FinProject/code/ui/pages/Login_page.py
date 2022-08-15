import allure

from code.ui.locators.LoginPage_locators import LoginPageLocators
from code.ui.pages.Base_page import BasePage
from code.ui.pages.Register_page import RegPage
from code.ui.pages.Main_page import MainPage

class LoginPage(BasePage):

    locators = LoginPageLocators

    @allure.step("Login {username}, {password}")
    def login(self, username, password):
        self.write(username, self.locators.LOGIN_INPUT_LOCATOR)
        self.write(password, self.locators.PASSWORD_INPUT_LOCATOR)
        self.click(self.locators.LOGIN_BUTTON_LOCATOR)
        return MainPage(self.browser, self.browser.current_url)

    @allure.step("Go to Reg Page")
    def go_to_register_page(self):
        self.click(self.locators.REG_BUTTON_LOCATOR)
        return RegPage(self.browser, self.browser.current_url)

    @allure.step("Check error of username or password")
    def username_or_password_alert(self):
        self.element_present(self.locators.WARNING_USERNAME_OR_PASSWORD_LOCATOR)

    @allure.step("Check error of lenght username or password")
    def username_lenght_alert(self):
        self.element_present(self.locators.WARNING_USERNAME_LENGTH_LOCATOR)
