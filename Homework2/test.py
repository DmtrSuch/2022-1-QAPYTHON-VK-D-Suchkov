import pytest
from UI.pages.base_page import PageNotOpenedException
from base import BaseCase
from UI.pages.login_page import LoginPage
from UI.pages.login_page import MainPage

COUNT = 10


class TestLogin(BaseCase):
    authorize = False


    @pytest.mark.UI
    @pytest.mark.parametrize('ex_number',range(2))
    def test_login(self,ex_number):
        self.logger.info('Login')
        user = self.random_text(COUNT)
        password = self.random_text(COUNT)
        with pytest.raises(PageNotOpenedException) as ex:
            assert LoginPage(self.driver).login(user, password)  # проверка в конструкторе




class TestCompany(BaseCase):
    authorize = False


    @pytest.mark.UI
    def test_create_company(self,credentials,file_path):
        name = self.random_text(COUNT)
        login_page = LoginPage(self.driver)
        main_page = login_page.login(*credentials)
        company_page = main_page.Go_To_Create_Company()
        company_page.CreateCompany(name, file_path)
        main_page.clickretry(main_page.locators.CHECK_MP_LOCATOR)
        assert name in company_page.driver.page_source

class TestSegment(BaseCase):

    @pytest.mark.UI
    def test_create_segment(self):
        name = self.random_text(COUNT)
        main_page = MainPage(self.driver)
        segment_page = main_page.Go_To_Segmetns()
        segment_page.CreateSegment(name)
        segment_page.clickretry(segment_page.locators.CHECK_LOCATOR)
        assert name in segment_page.driver.page_source
