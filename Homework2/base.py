
from contextlib import contextmanager


from _pytest.fixtures import FixtureRequest
from UI.fixtures import *
from UI.pages.main_page import MainPage

CLICK_RETRY = 3


class BaseCase:
    driver = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger
        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                if 'sameSite' in cookie:
                    if cookie['sameSite'] == 'None':
                        cookie['sameSite'] = 'Strict'
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.main_page = MainPage(driver)



        self.logger.debug('Initial setup done!')


