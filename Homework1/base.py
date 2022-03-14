import pytest
from _pytest.fixtures import FixtureRequest
from pages import *




class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config


        self.base_page:BasePage = (request.getfixturevalue('base_page'))
        self.main_page:MainPage = (request.getfixturevalue('main_page'))
        self.profile_page:ProfilePage = (request.getfixturevalue('profile_page'))
        self.billing_page:BillingPage = (request.getfixturevalue('billing_page'))
        self.tools_page:ToolsPage = (request.getfixturevalue('tools_page'))