import pytest
from code.config.creds import APP_SERVICE, APP_PORT
from code.api.api_client.api_client import ApiClient
import pdb


@pytest.fixture(scope="function")
def api_client():
    username = "Adminadmin"
    password = "Adminadmin"
    host = APP_SERVICE
    port = APP_PORT
    api_client = ApiClient(host, port, username, password)
    api_client.login()
    yield api_client
    api_client.logout()
