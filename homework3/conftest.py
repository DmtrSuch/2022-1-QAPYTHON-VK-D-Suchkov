import os
import pytest
import faker
from api.client import ApiClient

fake = faker.Faker()

def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com')

@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')

    return{
        'url':url
    }

@pytest.fixture(scope='function')
def api_client(config,credentials) -> ApiClient:
    return ApiClient(config['url'], *credentials)

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='session')
def credentials():
    with open('creds', 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password
