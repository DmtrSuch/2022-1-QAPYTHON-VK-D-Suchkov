from fixtures import *
import random
import string


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target.my.com')
    parser.addoption('--login', default='kksdf1@bk.ru')
    parser.addoption('--password', default='Bvcxz1234')
    parser.addoption('--fullname', default=''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(0,10))))
    parser.addoption('--number',default=random.randint(100000,999999))



@pytest.fixture()
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')
    fullname = request.config.getoption('--fullname')
    number = request.config.getoption('--number')

    return {'browser': browser, 'url': url, 'login':login,'password':password,'fullname':fullname,'number':number}

