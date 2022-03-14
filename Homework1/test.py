import pytest
from base import BaseCase
from locators import MainPageLocators
from locators import BillingPageLocators
from locators import ToolsPageLocators


class TestExample(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.base_page.login()
        assert self.main_page.find(self.main_page.locators.INSTRUCTION_MODULE_TITLE_LOCATOR
        ).text in self.driver.page_source

    @pytest.mark.UI
    def test_logout(self):
        self.main_page.login()
        self.main_page.logout()
        assert self.base_page.find(self.base_page.locators.BASEPAGE_BIGTITLE_LOCATOR
        ).text in self.driver.page_source

    @pytest.mark.UI
    def test_changeinfo(self):
        self.main_page.login()
        self.main_page.clickretry(self.profile_page.locators.PROFILE_LOCATOR)
        self.profile_page.changerandominfo()
        self.profile_page.clickretry(self.profile_page.locators.SUCCESSSAVE_LOCATOR)
        assert self.profile_page.find(self.profile_page.locators.SUCCESSSAVE_LOCATOR
        ).text in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "INlocator,CHCKlocator",
        [
            pytest.param(
                MainPageLocators.BILLING_LOCATOR,
                BillingPageLocators.SUBTITLE_BILLING_LOCATOR,
            ),
            pytest.param(
                MainPageLocators.TOOLS_LOCATOR,
                ToolsPageLocators.TOOLS_FEEDS_LOCATOR,
            ),
        ],
    )
    def test_transition(self,INlocator,CHCKlocator):
        self.base_page.login()
        self.base_page.clickretry(INlocator)
        self.base_page.clickretry(CHCKlocator)
        assert self.base_page.find(CHCKlocator).text in self.driver.page_source