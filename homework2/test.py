import os

import pytest

from base import BaseCase
from ui.locators import basic_locators
from base import get_random_info
from selenium.webdriver.common.by import By

'''
            login_page
            |
base_page --
            |
            main_page --[dashboard_page, segments_page, ]
'''


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip
    def test_negative_auth_one(self, credentials):
        self.login_page.login(email=credentials[0], password=credentials[0])
        assert self.driver.current_url == f'https://account.my.com/login/?error_code=1&email={credentials[0]}&continue' \
        f'=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1%23email'

    @pytest.mark.skip
    def test_negative_auth_two(self, credentials):
        self.authorize = False
        self.login_page.login(email=credentials[0], password=credentials[0])
        message = self.login_page.find(basic_locators.LoginPageLocators.ERROR_LOGIN_MESSAGE)
        assert message.text == 'Error'


class Test(BaseCase):
    authorize = True

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'image.png')

    @pytest.mark.skip
    def test_create_ad_campaign(self, file_path):
        url_of_the_advertised_object = 'https://www.google.com/'
        campaign_name = get_random_info(10)

        self.logger.info('Authorization. Going to dashboard page.')
        self.logger.info('Creating new ad campaign.')

        self.dashboard_page.create_ad_campaign(file_path, url_of_the_advertised_object, campaign_name)
        self.dashboard_page.url_matches('https://target.my.com/dashboard#')

        TITLE_CAMPAIGN_LOCATOR = (By.XPATH, f'//a[@title="{campaign_name}"]')
        elem_title = self.dashboard_page.find(TITLE_CAMPAIGN_LOCATOR)

        assert elem_title.get_attribute('text') == campaign_name
        # assert self.dashboard_page.find(basic_locators.DashboardPageLocators.MESSAGE_ABOUT_SUCCESSFUL_CREATION)

    @pytest.mark.skip
    def test_create_segment(self):
        name_segment = get_random_info(10)

        self.logger.info('Authorization. Going to dashboard page.')
        self.logger.info('Going to segments page.')

        self.segments_page = self.dashboard_page.go_to_segments()

        self.logger.info('Creating new segment.')

        self.segments_page.create_new_segment(name_segment)

        CHECK_TITLE_NEW_SEGMENT_LOCATOR = (By.XPATH, f'//a[@title="{name_segment}"]')
        elem_title = self.segments_page.find(CHECK_TITLE_NEW_SEGMENT_LOCATOR)

        assert elem_title.get_attribute('text') == name_segment

    @pytest.mark.skip
    def test_delete_segment(self):
        name_segment = get_random_info(10)

        self.logger.info('Authorization. Going to dashboard page.')
        self.logger.info('Going to segments page.')

        self.segments_page = self.dashboard_page.go_to_segments()

        self.logger.info('Creating new segment.')

        self.segments_page.create_new_segment(name_segment)

        self.logger.info('Deleting new segment.')

        CHECK_TITLE_NEW_SEGMENT_LOCATOR = (By.XPATH, f'//a[@title="{name_segment}"]')  #
        elem_title = self.segments_page.find(CHECK_TITLE_NEW_SEGMENT_LOCATOR)  #

        self.segments_page.delete_segment(name_segment)

        assert self.segments_page.element_not_present(elem_title)


