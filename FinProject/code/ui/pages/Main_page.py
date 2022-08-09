import allure

from code.ui.enums.navbar_names import *
from code.ui.enums.block_names import *
from code.ui.locators.MainPage_locators import MainPageLocators
from code.ui.pages.Base_page import BasePage
import code.ui.pages.Login_page as LP

class MainPage(BasePage):

    locators = MainPageLocators

    @allure.step("Logout")
    def logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
        return LP.LoginPage(self.browser, self.browser.current_url)

    @allure.step("Go to link from navbar")
    def navbar_link(self, link_name: NavbarLinkNames):
        self.move_to_element(NavbarLinkListButtonLocator.Items.get(link_name))
        self.click(NavbarLinkButtonLocator.Items.get(link_name))
        self.browser.switch_to.window(self.browser.window_handles[-1])

    @allure.step("Check link from navbar")
    def navbar_link_correct_url(self, page_name: NavbarLinkNames):
        link = self.browser.current_url
        assert(link, page_name) in NavbarLinkUrl.Items.items()

    @allure.step("Go to link from block")
    def block_link(self, link_name: BlockLinkNames):
        self.click(ListBlockLinkLocators.Items.get(link_name))
        self.browser.switch_to.window(self.browser.window_handles[-1])

    @allure.step("Check link from block")
    def block_link_correct_url(self, page_name :BlockLinkNames):
        link = self.browser.current_url
        assert (link, page_name) in ListBLockLinkURL.Items.items()

    @allure.step("Go to link python")
    def go_python(self):
        self.click(self.locators.PYTHON_LINK)
        assert (self.browser.current_url, NavbarLinkNames.PYTHON) in NavbarLinkUrl.Items.items()
