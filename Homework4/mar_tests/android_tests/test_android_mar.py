import time
import allure
import pytest
import random
from mar_tests.base import BaseCase



class TestAndroid(BaseCase):

    @pytest.mark.AndroidUI
    def test_population(self):
        self.main_page.skip_notification()
        self.main_page.use_keyboard()
        self.main_page.search('Russia')
        self.main_page.swipe_element_lo_left(self.main_page.locators.SWIPE_POPULATION)
        self.main_page.click_for_android(self.main_page.locators.SWIPE_CLICK)
        assert self.main_page.find(self.main_page.locators.BIG_ANSWER_LOCATOR).text in self.driver.page_source

    @pytest.mark.AndroidUI
    def test_calc(self):
        self.main_page.skip_notification()
        self.main_page.use_keyboard()
        self.main_page.search(f'{random.randint(0,999)}+{random.randint(0,999)}')

    @pytest.mark.AndroidUI
    def test_news(self):
        self.main_page.skip_notification()
        self.main_page.go_to_menu()
        self.menu_page.changenews()
        self.menu_page.exit()
        self.main_page.use_keyboard()
        self.main_page.search('News')
        assert self.main_page.find(self.main_page.locators.TURN_NEWS1_LOCATION).text \
        or self.main_page.find(self.main_page.locators.TURN_NEWS2_LOCATION).text \
        or self.main_page.find(self.main_page.locators.PLAY_NEWS_LOCATION).text \
        in self.driver.page_source


    @pytest.mark.AndroidUI
    def test_version(self):
        FILENAME = self.driver.desired_capabilities['app']
        FILEVERSION = FILENAME.split('/')[-1].split('v')[1].split('.a')[0]
        self.main_page.skip_notification()
        self.main_page.go_to_menu()
        self.menu_page.checkversion()
        assert self.menu_page.find(self.menu_page.locators.COPYRIGHT_LOCATOR).text in self.driver.page_source
        assert FILEVERSION in self.menu_page.find(self.menu_page.locators.VERSION_APP_LOCATOR).text
