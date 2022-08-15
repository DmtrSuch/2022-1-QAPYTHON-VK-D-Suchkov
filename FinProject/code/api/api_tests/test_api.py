import allure
import pytest

from code.conftest import MySql
from code.api.conftest import api_client
from code.mock_api.api_vk_client import VkApiClient
from code.utils.userbuilder import UserBuilder, User
from code.config.creds import APP_SERVICE, APP_PORT

class TestClass(MySql):

    @allure.epic('API tests')
    @allure.title('Correct user login')
    @allure.description(
        """
        Test login 
        """
    )
    def test_login(self, api_client):
        res = api_client.login()
        assert len(self.client.get_current_user()) == 1
        assert res.headers['location'] == f'http://{APP_SERVICE}:{APP_PORT}/welcome/'
        assert res.status_code == 302


    @allure.epic('API tests')
    @allure.title('Incorrect user login')
    @allure.description(
        """
        Test negative invalidlogin
        !BUG!
        """
    )
    @pytest.mark.xfail
    @pytest.mark.parametrize('username, password', [('invalidusername','invalidPassword')])
    def test_invalid_login(self, api_client, username, password):
        res = api_client.invalidlogin(username, password)
        assert res.url == f'http://{APP_SERVICE}:{APP_PORT}/login'
        assert res.status_code == 404

    @allure.epic('API tests')
    @allure.title('Login with invalid password')
    @allure.description(
        """
        Test negative invalidlogin with invalid password
        !BUG! 
        """
    )
    @pytest.mark.xfail
    @pytest.mark.parametrize('password', ["invalidPassword"])
    def test_invalid_password_login(self, api_client, password):
        res = api_client.invalidlogin("Adminadmin", password)
        assert res.status_code == 404

    @allure.epic('API tests')
    @allure.title('Empty login')
    @allure.description(
        """
        Test empty login
        !BUG! 
        """
    )
    @pytest.mark.xfail
    @pytest.mark.parametrize('username, password',[('',''), (' ', ' ')])
    def test_empty_password_login(self, api_client, username, password):
        res = api_client.invalidlogin(username, password)
        assert res.status_code == 401

    @allure.epic('API tests')
    @allure.title('Add user')
    @allure.description(
        """
        Test add user
        !BUG! 
        """
    )
    @pytest.mark.xfail
    def test_add_user(self, api_client):
        UB = UserBuilder()
        user = UB.create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        res = api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                                  user.email, user.password)
        assert res.status_code == 201
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 1

    @allure.epic('API tests')
    @allure.title('Add user without middle name')
    @allure.description(
        """
        Test add user without middle name
        !BUG!
        """
    )
    @pytest.mark.xfail
    def test_add_user_without_middlename(self, api_client):
        UB = UserBuilder()
        user = UB.create_user()
        user.Midddleename = None
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        res = api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                                  user.email, user.password)
        assert res.status_code == 201
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 1

    @allure.epic('API tests')
    @allure.title('Add user with long name, email, password')
    @allure.description(
        """
        Test add user with long name, long email, long password
        !BUG! 
        """
    )
    @pytest.mark.xfail
    @pytest.mark.parametrize("user", [UserBuilder.create_user(length_name = 256), \
                                      UserBuilder.create_user(length_surname = 256), \
                                      UserBuilder.create_user(length_middleename = 256), \
                                      UserBuilder.create_user(length_username = 17), \
                                      UserBuilder.create_user(length_email = 65), \
                                      UserBuilder.create_user(length_password = 256)])
    def test_add_user_with_longname(self, api_client, user):
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        res = api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                                  user.email, user.password)
        assert res.status_code == 400
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0

    @allure.epic('API tests')
    @allure.title('Delete user')
    @allure.description(
        """
        Test delete user
        """
    )
    def test_delete_user(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 1
        res = api_client.delete_user(user.username)
        assert res.status_code == 204
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0

    @allure.epic('API tests')
    @allure.title('Delete non exist user')
    @allure.description(
        """
        Test delete non exist user
        """
    )
    def test_non_exist_delete_user(self, api_client):
        user = UserBuilder.create_user()
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0
        res = api_client.delete_user(user.username)
        assert res.status_code == 404
        users_count_with_this_name = len(self.client.get_users_by_username(user.username))
        assert users_count_with_this_name == 0

    @allure.epic('API tests')
    @allure.title('Change pass')
    @allure.description(
        """
        Change password
        !BUG!
        """
    )
    @pytest.mark.xfail
    def test_change_user_password(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        new_password = UserBuilder.create_user().password
        res = api_client.change_password(user.username, new_password)
        db_user = self.client.get_users_by_username(user.username)[0]
        assert db_user.password == new_password
        assert res.status_code == 200

    @allure.epic('API tests')
    @allure.title('Incorrect change pass')
    @allure.description(
        """
        Incorrect change password
        !BUG!
        """
    )
    @pytest.mark.xfail
    def test_incorrect_change_user_password(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        new_password = ' '
        res = api_client.change_password(user.username, new_password)
        db_user = self.client.get_users_by_username(user.username)[0]
        assert db_user.password == new_password
        assert res.status_code == 200

    @allure.epic('API tests')
    @allure.title('Repeat change pass')
    @allure.description(
        """
        Repeat change password
        """
    )
    def test_repeat_changre_user_password(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        res = api_client.change_password(user.username, user.password)
        db_user = self.client.get_users_by_username(user.username)[0]
        assert db_user.password == user.password
        assert res.status_code == 400

    @allure.epic('API tests')
    @allure.title('Block user')
    @allure.description(
        """
        Block user
        """
    )
    def test_block(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        access_user = self.client.get_users_by_username(user.username)[0].access
        assert access_user == 1
        res = api_client.block_user(user.username)
        assert res.status_code == 200
        access_user = self.client.get_users_by_username(user.username)[0].access
        assert access_user == 0

    @allure.epic('API tests')
    @allure.title('Unblock user')
    @allure.description(
        """
        Unblock user
        """
    )
    def test_unblock(self, api_client):
        user = UserBuilder.create_user()
        api_client.add_user(user.name, user.surname, user.Midddleename, user.username, \
                            user.email, user.password)
        api_client.block_user(user.username)
        res = api_client.unblock_user(user.username)
        assert res.status_code == 200
        access_user = self.client.get_users_by_username(user.username)[0].access
        assert access_user == 1

    @allure.epic('API tests')
    @allure.title('Get status')
    @allure.description(
        """
        Get status
        """
    )
    def test_get_status(self, api_client):
        res = api_client.status()
        assert res.status_code == 200
        assert res.json()['status'] == 'ok'