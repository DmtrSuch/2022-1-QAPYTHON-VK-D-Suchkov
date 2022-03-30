import faker
import pytest
from UI.pages.base_page import PageNotOpenedException
from base import BaseCase
from UI.pages.login_page import LoginPage
from UI.pages.login_page import MainPage





class TestLogin(BaseCase):
    authorize = False
    fake = faker.Faker()

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "user,password",
        [
            pytest.param(
                fake.lexify(text = '?????'),
                fake.lexify(text='?????????'),
            ),
            pytest.param(
                fake.lexify(text='???????'),
                fake.lexify(text='??????????'),
            ),
        ]
    )
    def test_login(self,user,password):
        self.logger.info('Login')
        try:
            assert LoginPage(self.driver).login(user,password)#проверка в конструкторе
        except PageNotOpenedException:
            pass



class TestCompany(BaseCase):
    authorize = False

    @pytest.mark.UI
    def test_create(self,credentials,file_path):
        fake = faker.Faker()
        name = fake.lexify(text='???????')
        login_page = LoginPage(self.driver)
        main_page = login_page.login(*credentials)
        company_page = main_page.Go_To_Create_Company()
        company_page.CreateCompany(name,file_path)
        main_page.clickretry(main_page.locators.CHECK_MP_LOCATOR)
        assert name in company_page.driver.page_source

class TestSegment(BaseCase):

    @pytest.mark.UI
    def test_create(self):
        fake = faker.Faker()
        name = fake.lexify(text='???????')
        main_page = MainPage(self.driver)
        segment_page = main_page.Go_To_Segmetns()
        segment_page.CreateSegment(name)

        assert name in segment_page.driver.page_source


    @pytest.mark.UI
    def test_delete(self):
        pass