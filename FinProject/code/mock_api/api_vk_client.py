import json
import logging

import requests
LOGGER = logging.getLogger('test')

class VkApiClient:

    def __init__(self, hostname = "finproject_vk_mock_1", port="5000"):
        self.hostname = hostname
        self.port = port

        self.session = requests.Session()

    def get_user(self, username):
        LOGGER.info("GET user info", username)
        response = self.session.get(f'http://{self.hostname}:{self.port}/vk_id/{username}')
        LOGGER.info(response.headers)
        LOGGER.info(response.status_code)
        LOGGER.info(response.text)
        return response

    def post_add_user(self, username):
        LOGGER.info("ADD USER ", username)
        url = f"http://{self.hostname}:{self.port}/vk_id/add_user"
        body = json.dumps({"name": username})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=body, verify=False)
        LOGGER.info(response.headers)
        LOGGER.info(response.status_code)
        LOGGER.info(response.text)

