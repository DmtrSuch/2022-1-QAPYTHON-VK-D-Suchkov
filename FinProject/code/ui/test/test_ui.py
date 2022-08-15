import allure
import pytest

from code.conftest import MySql
from code.api.api_client.api_client import ApiClient, VkApiClient
from code.ui.locators.LoginPage_locators import LoginPageLocators
from code.ui.locators.MainPage_locators import MainPageLocators
from code.ui.locators.RegPage_locators import RegPageLocators
from code.config.creds import APP_SERVICE, APP_PORT
from code.utils.userbuilder import UserBuilder, User
from code.mysql.builder import MysqlBuilder
from code.ui.enums.block_names import BlockLinkNames
from code.ui.enums.navbar_names import NavbarLinkNames

MAIN_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/welcome/"
REG_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/reg"
LOGIN_PAGE_URL = f"http://{APP_SERVICE}:{APP_PORT}/login"

API = VkApiClient()

class TestLoginPage(MySql):

    @allure.epic('UI tests')
    @allure.title('Login')
    @allure.description(
        """
            Test  login
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_login(self, login_page):
        login_page.login("Adminadmin", "Adminadmin")
        assert login_page.browser.current_url == MAIN_PAGE_URL

        user = self.client.get_users_by_username("Adminadmin")[0]
        assert user.active == 1

    @allure.epic('UI tests')
    @allure.title('Invalid login')
    @allure.description(
        """
            Test invalid login
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    @pytest.mark.parametrize('username, password', [(UserBuilder.create_user().username, \
                                                    UserBuilder.create_user().password)])
    def test_invalid_login(self, login_page, username, password):
        login_page.login(username, password)
        assert login_page.text_present(login_page.locators.WARNING_USERNAME_OR_PASSWORD_LOCATOR,"Invalid")
        assert login_page.browser.current_url == LOGIN_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Go to reg page')
    @allure.description(
        """
            Test go to reg pag
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_go_to_reg_page(self, login_page):
        RegPage = login_page.go_to_register_page()
        assert RegPage.url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Short login')
    @allure.description(
        """
            Test short login
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_short_login(self, login_page):
        login_page.login(' ',' ')
        assert "6" in login_page.find(login_page.locators.LOGIN_INPUT_LOCATOR).get_attribute('validationMessage')

    @allure.epic('UI tests')
    @allure.title('Empty login')
    @allure.description(
        """
            Empty login
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_empty_login(self, login_page):
        login_page.login('', '')
        assert "поле" in login_page.find(login_page.locators.LOGIN_INPUT_LOCATOR).get_attribute('validationMessage')

    @allure.epic('UI tests')
    @allure.title('Empty password')
    @allure.description(
        """
            Empty password
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_empty_pass(self, login_page):
        login_page.login('Adminadmin', '')
        assert "поле" in login_page.find(login_page.locators.PASSWORD_INPUT_LOCATOR).get_attribute('validationMessage')

    @allure.epic('UI tests')
    @allure.title('Test block user login')
    @allure.description(
        """
            Test block user login
        """
    )
    @pytest.mark.login
    @pytest.mark.noautologin
    def test_login_block_user(self, login_page):
        user = UserBuilder.create_user()
        self.builder.add_user(user.name,user.surname,user.username, \
                              user.email,user.password,user.Midddleename, 0)
        login_page.login(user.username, user.password)
        assert login_page.text_present(login_page.locators.WARNING_ACC_BLOCK, "запись")


class TestRegPage(MySql):
    @allure.epic('UI tests')
    @allure.title('Go login page')
    @allure.description(
        """
            Test go login page
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    def test_go_login_page(self, register_page):
        register_page.go_login_page()
        assert register_page.browser.current_url == LOGIN_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user')
    @allure.description(
        """
            Create user
            !BUG!
            middlename non in DB
        """
    )
    @pytest.mark.reg
    @pytest.mark.xfail
    @pytest.mark.noautologin
    def test_create_user(self, register_page):
        user = UserBuilder.create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        MP = register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                               user.Midddleename)
        assert MP.browser.current_url == MAIN_PAGE_URL
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 1
        assert MP.text_present(MP.locators.VK_ID_TEXT,API.get_user(user.username).text.split('"')[3])
        assert self.client.user_was_created_with_right_data(user.username, user)

    @allure.epic('UI tests')
    @allure.title('Create user with Empty Name, Surname, Username, Password')
    @allure.description(
        """
            incorrect Name, Surname, Username, Password
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    @pytest.mark.parametrize('user, locator', [(UserBuilder.create_user(name=''), RegPageLocators.NAME_INPUT_LOCATOR), \
                                               (UserBuilder.create_user(surname=''), RegPageLocators.SURNAME_INPUT_LOCATOR), \
                                               (UserBuilder.create_user(username=''), RegPageLocators.USERNAME_INPUT_LOCATOR), \
                                               (UserBuilder.create_user(), RegPageLocators.PASSWORD_INPUT_LOCATOR)])
    def test_create_user_empty(self, register_page, user, locator):
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, '', \
                                    user.Midddleename)
        assert register_page.browser.current_url == REG_PAGE_URL
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert "поле" in register_page.find(locator).get_attribute('validationMessage')

    @allure.epic('UI tests')
    @allure.title('Create user without Middlename')
    @allure.description(
        """
            Create user
            !BUG!
        """
    )
    @pytest.mark.reg
    @pytest.mark.xfail
    @pytest.mark.noautologin
    def test_create_user_without_middlename(self, register_page):
        user = UserBuilder.create_user(Midddleename='')
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                                    user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert self.client.user_was_created_with_right_data(user.username, user)
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with max symbol')
    @allure.description(
        """
            Create user with max symbol
            without middlename
            !BUG!
            name symbols < 255
        """
    )
    @pytest.mark.reg
    @pytest.mark.xfail
    @pytest.mark.noautologin
    def test_create_user_with_max_symbol(self, register_page):
        user = UserBuilder.create_user(length_name = 255, length_surname = 255, Midddleename = None, \
                                       length_username = 16, length_password = 255, length_email = 64 )
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        MP = register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                               user.Midddleename)
        assert MP.browser.current_url == MAIN_PAGE_URL
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 1
        assert MP.text_present(MP.locators.VK_ID_TEXT, API.get_user(user.username).text.split('"')[3])
        assert self.client.user_was_created_with_right_data(user.username, user)

    @allure.epic('UI tests')
    @allure.title('Create user with over symbol')
    @allure.description(
        """
            Create user with over symbol
            without middlename
            !BUG!
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    @pytest.mark.parametrize('user', [(UserBuilder.create_user(length_surname = 256)), \
                                      (UserBuilder.create_user(length_password= 256))])
    def test_create_user_with_over_symbol(self, register_page, user):
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                               user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with exist username')
    @allure.description(
        """
            Create user with exist username
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    def test_create_user_with_exist_username(self, register_page):
        user1 = UserBuilder().create_user()
        self.builder.add_user(user1.name,user1.surname,user1.username,user1.email,user1.password,user1.Midddleename)
        user = UserBuilder().create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user1.username, user.email, user.password, user.password, \
                               user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert register_page.text_present(register_page.locators.ALLERT_LOCATOR, 'User already')
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with exist email')
    @allure.description(
        """
            Create user with exist email
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    def test_create_user_with_exist_email(self, register_page):
        user1 = UserBuilder().create_user()
        self.builder.add_user(user1.name, user1.surname, user1.username, user1.email, user1.password,
                              user1.Midddleename)
        user = UserBuilder().create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user1.email, user.password, user.password, \
                               user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert register_page.text_present(register_page.locators.ALLERT_LOCATOR, 'Internal Server Error')
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with non match pass')
    @allure.description(
        """
            Create user with non match pass
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    def test_create_user_with_non_match_pass(self, register_page):
        user = UserBuilder().create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password+'1', \
                               user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert register_page.text_present(register_page.locators.ALLERT_LOCATOR, 'Passwords must match')
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with non accept checkbox')
    @allure.description(
        """
            Create user with non accept checkbox
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    def test_create_user_with_non_accept_checkbox(self, register_page):
        user = UserBuilder().create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                               user.Midddleename, accept= False)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert 'флажок'in register_page.find(register_page.locators.CONFIRM_CHECKBOX_LOCATOR). \
            get_attribute('validationMessage')
        assert register_page.browser.current_url == REG_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Create user with username/email < 6 symbols')
    @allure.description(
        """
            Create user with username/email < 6 symbols
        """
    )
    @pytest.mark.reg
    @pytest.mark.noautologin
    @pytest.mark.parametrize('user, locator', [(UserBuilder.create_user(length_username = 5),\
                                                RegPageLocators.USERNAME_INPUT_LOCATOR), \
                                                (UserBuilder.create_user(email="a@b.u"), \
                                                RegPageLocators.EMAIL_INPUT_LOCATOR)])
    def test_create_user_with_non_accept_checkbox(self, register_page, user, locator):
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        register_page.register(user.name, user.surname, user.username, user.email, user.password, user.password, \
                               user.Midddleename)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        assert '6'in register_page.find(locator).get_attribute('validationMessage')
        assert register_page.browser.current_url == REG_PAGE_URL

class TestMainPage(MySql):
    @allure.epic('UI tests')
    @allure.title('Logout')
    @allure.description(
        """
            Logout
        """
    )
    @pytest.mark.main
    def test_logout(self, main_page):
        user = self.client.get_users_by_username("Adminadmin")[0]
        assert user.active == 1
        LP = main_page.logout()
        user = self.client.get_users_by_username("Adminadmin")[0]
        assert user.active == 0
        assert LP.browser.current_url == LOGIN_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Logout long surname')
    @allure.description(
        """
            Logout with long surname
            !BUG!
        """
    )
    @pytest.mark.noautologin
    @pytest.mark.main
    @pytest.mark.xfail
    def test_logout_with_long_surname(self, login_page):
        user = UserBuilder.create_user(length_surname=255)
        self.builder.add_user(user.name, user.surname, user.username, user.email, user.password,
                              user.Midddleename)
        MP = login_page.login(user.username, user.password)
        LP = MP.logout()
        assert LP.browser.current_url == LOGIN_PAGE_URL

    @allure.epic('UI tests')
    @allure.title('Navbar with long surname')
    @allure.description(
        """
            Navbar with long surname
            !BUG!
        """
    )
    @pytest.mark.noautologin
    @pytest.mark.main
    @pytest.mark.xfail
    @pytest.mark.parametrize("link_name", [
        NavbarLinkNames.PYTHON_HISTORY,
        NavbarLinkNames.FLASK,
        NavbarLinkNames.CENTOS,
        NavbarLinkNames.WIRESHARK_NEWS,
        NavbarLinkNames.WIRESHARK_DOWNLOAD,
        NavbarLinkNames.TCPDUMP_EXAMPLES])
    def test_navbar_with_long_surname(self, login_page, link_name):
        user = UserBuilder.create_user(length_surname=255)
        self.builder.add_user(user.name, user.surname, user.username, user.email, user.password,
                              user.Midddleename)
        MP = login_page.login(user.username, user.password)
        MP.navbar_link(link_name)
        MP.navbar_link_correct_url(link_name)

    @allure.epic('UI tests')
    @allure.title('Go navbar links')
    @allure.description(
        """
            Check link in navbar
        """
    )
    @pytest.mark.main
    @pytest.mark.parametrize("link_name", [
        NavbarLinkNames.PYTHON_HISTORY,
        NavbarLinkNames.FLASK,
        NavbarLinkNames.CENTOS,
        NavbarLinkNames.WIRESHARK_NEWS,
        NavbarLinkNames.WIRESHARK_DOWNLOAD,
        NavbarLinkNames.TCPDUMP_EXAMPLES])
    def test_go_navbar_link(self, main_page, link_name):
        main_page.navbar_link(link_name)
        main_page.navbar_link_correct_url(link_name)

    @allure.epic('UI tests')
    @allure.title('Go block links')
    @allure.description(
        """
            Check block links
        """
    )
    @pytest.mark.main
    @pytest.mark.parametrize("link_name", [
        BlockLinkNames.API,
        BlockLinkNames.INTERNET,
        BlockLinkNames.SMTP
    ])
    def test_go_block_link(self, main_page, link_name):
        main_page.block_link(link_name)
        main_page.block_link_correct_url(link_name)

    @allure.epic('UI tests')
    @allure.title('Go python')
    @allure.description(
        """
            Check python
        """
    )
    @pytest.mark.main
    def test_go_python(self, main_page):
        main_page.go_python()
