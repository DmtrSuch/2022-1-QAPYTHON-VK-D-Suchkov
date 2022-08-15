import allure

import code.ui.pages.Login_page as LP
import code.ui.pages.Main_page as MP
from code.utils.userbuilder import UserBuilder, User
from code.ui.locators.RegPage_locators import RegPageLocators
from code.ui.pages.Base_page import BasePage


class RegPage(BasePage):

    locators = RegPageLocators

    @allure.step("Go to login page across logout")
    def go_login_page(self):
        self.click(self.locators.LOGIN_LOCATOR)
        return LP.LoginPage(self.browser, self.browser.current_url)

    @allure.step("Register")
    def register(self, name, surname, username, email, password, confirm_password, middle_name, accept = True):
        self.write(name, self.locators.NAME_INPUT_LOCATOR)
        self.write(surname, self.locators.SURNAME_INPUT_LOCATOR)
        self.write(middle_name,self.locators.MIDDLENAME_INPUT_LOCATOR)
        self.write(username, self.locators.USERNAME_INPUT_LOCATOR)
        self.write(email, self.locators.EMAIL_INPUT_LOCATOR)
        self.write(password, self.locators.PASSWORD_INPUT_LOCATOR)
        self.write(confirm_password, self.locators.CONFIRM_PASSWORD_INPUT_LOCATOR)
        if accept:
            self.click(self.locators.CONFIRM_CHECKBOX_LOCATOR)
        self.API.post_add_user(username)
        self.click(self.locators.SUBMIT_BUTTON_LOCATOR)
        return MP.MainPage(self.browser, self.browser.current_url)
