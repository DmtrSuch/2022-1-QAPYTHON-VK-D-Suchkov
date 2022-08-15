import json

import allure

from code.mock_api.api_vk_client import VkApiClient
from urllib.parse import urljoin
import requests
import pdb



class ApiClient:
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"


    def __init__(self, host, port, username, password):
        self.session = requests.Session()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.url = "http://" + self.host + ":" + str(self.port)
        self.cookies = None
        self.API = VkApiClient()

    @allure.step("Send {method} request to {location}")
    def _request(self, method, url=None, location=None, headers=None, params=None, data=None, json=False,
                 allow_redirects=False):
        if location is not None and url is None:
            url = urljoin(self.url, location)

        res = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            allow_redirects=allow_redirects
        )
        if json:
            return res.json()
        else:
            return res

    @allure.step("Invalid login with {username} and {password}")
    def invalidlogin(self, username, password):
        location = "/login"
        headers = {
            'Referer': f'http://{self.url}/login'
        }
        body = {
            'username': username,
            'password': password
        }
        response = self._request(method=self.POST, location=location, headers=headers, data=body)
        self.cookies = response.headers['Set-Cookie'].split(';')[0]
        return response

    @allure.step("Default login")
    def login(self):
        return self.invalidlogin(self.username, self.password)

    @allure.step("Logout")
    def logout(self):
        location = "/logout"
        response = self._request(method=self.GET, location=location)
        return response

    @allure.step("Status")
    def status(self):
        location = "/status"
        response = self._request(method=self.GET, location=location)
        return response

    @allure.step("Delete users")
    def delete_user(self, username):
        location = "/api/user/" + username
        response = self._request(method=self.DELETE, location=location)
        return response

    @allure.step("Add user")
    def add_user(self, name, surname, middleename, username, email, password):
        location = "/api/user"
        content_type = "application/json"

        headers = {
            'Content-Type': content_type,
            'Cookie': self.cookies,
        }

        body = {
            'name': name,
            'surname':surname,
            'middle_name':middleename,
            'username': username,
            'email': email,
            'password': password,
            'confirm': password,
            'term': 'y',
            'submit':'Register'
        }
        body = json.dumps(body)
        self.API.post_add_user(username)
        response = self._request(method=self.POST, location=location, headers=headers, data=body)
        return response

    @allure.step("Change password")
    def change_password(self ,username, password):
        location = "/api/user/" + username + '/change-password'
        content_type = "application/json"

        headers = {
            'Content-Type': content_type,
            'Cookie': self.cookies,
        }

        body = {
            'password': password,
        }
        body = json.dumps(body)
        response = self._request(method=self.PUT, location=location, headers=headers, data=body)
        return response

    @allure.step("Block user")
    def block_user(self, username):
        location = "/api/user/" + username + "/block"
        response = self._request(method=self.POST, location=location)
        return response

    @allure.step("Unblock user")
    def unblock_user(self, username):
        location = "/api/user/" + username + "/accept"
        response = self._request(method=self.POST, location=location)
        return response

