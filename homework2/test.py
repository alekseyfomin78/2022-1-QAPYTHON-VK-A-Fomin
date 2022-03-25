import os

import pytest

from base import BaseCase
from base import get_random_info
from selenium.webdriver.common.by import By

from ui.pages.login_page import ErrorLoginException

'''
Структура страниц:

             --> login_page
             |
base_page -->
             |
             --> main_page --> [dashboard_page, segments_page, ]
'''


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.UI
    def test_negative_login_one(self, credentials):
        self.logger.info(f'Opening login page "{self.login_page.url}"')

        self.logger.info('Login')

        self.logger.info('Checking that login is not correct')

        with pytest.raises(ErrorLoginException):
            self.login_page.login(email=credentials[0], password=credentials[0])

    @pytest.mark.UI
    def test_negative_login_two(self, credentials):
        self.logger.info(f'Opening login page "{self.login_page.url}"')

        self.logger.info('Login')

        self.logger.info('Checking that login is not correct')

        with pytest.raises(ErrorLoginException):
            self.login_page.login(email=credentials[1], password=credentials[1])


class Test(BaseCase):
    authorize = True

    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'image.png')

    @pytest.mark.UI
    def test_create_ad_campaign(self, file_path):
        url_of_the_advertised_object = 'https://www.google.com/'
        campaign_name = get_random_info(10)

        self.logger.info(f'Opening login page "{self.login_page.url}"')
        self.logger.info('Login')
        self.logger.info(f'Going to dashboard page "{self.dashboard_page.url}"')
        self.logger.info(f'Creating new advertisement campaign "{campaign_name}"')

        self.dashboard_page.create_ad_campaign(file_path, url_of_the_advertised_object, campaign_name)
        self.dashboard_page.url_matches('https://target.my.com/dashboard#')

        self.logger.info(f'New advertisement campaign "{campaign_name}" is created')

        CHECK_TITLE_CAMPAIGN_LOCATOR = (By.XPATH, f'//a[@title="{campaign_name}"]')
        elem_title = self.dashboard_page.find(CHECK_TITLE_CAMPAIGN_LOCATOR, timeout=60)

        self.logger.info(f'Checking that the advertisement campaign "{campaign_name}" has been created')

        assert elem_title.get_attribute('text') == campaign_name

    @pytest.mark.UI
    def test_create_segment(self):
        name_segment = get_random_info(10)

        self.logger.info(f'Opening login page "{self.login_page.url}"')
        self.logger.info('Login')
        self.logger.info(f'Going to dashboard page "{self.dashboard_page.url}"')

        self.segments_page = self.dashboard_page.go_to_segments()

        self.logger.info(f'Going to segments page "{self.segments_page.url}"')
        self.logger.info(f'Creating new segment "{name_segment}"')

        self.segments_page.create_new_segment(name_segment)

        self.logger.info(f'New segment "{name_segment}" is created')

        CHECK_TITLE_NEW_SEGMENT_LOCATOR = (By.XPATH, f'//a[@title="{name_segment}"]')
        elem_title = self.segments_page.find(CHECK_TITLE_NEW_SEGMENT_LOCATOR)

        self.logger.info(f'Checking that the segment "{name_segment}" has been created')

        assert elem_title.get_attribute('text') == name_segment

    @pytest.mark.UI
    def test_delete_segment(self):
        name_segment = get_random_info(10)

        self.logger.info(f'Opening login page "{self.login_page.url}"')
        self.logger.info('Login')
        self.logger.info(f'Going to dashboard page "{self.dashboard_page.url}"')

        self.segments_page = self.dashboard_page.go_to_segments()

        self.logger.info(f'Going to segments page "{self.segments_page.url}"')
        self.logger.info(f'Creating new segment "{name_segment}"')

        self.segments_page.create_new_segment(name_segment)

        self.logger.info(f'New segment "{name_segment}" is created')
        self.logger.info(f'Deleting segment "{name_segment}"')

        CHECK_TITLE_NEW_SEGMENT_LOCATOR = (By.XPATH, f'//a[@title="{name_segment}"]')  #
        elem_title = self.segments_page.find(CHECK_TITLE_NEW_SEGMENT_LOCATOR)  #

        self.segments_page.delete_segment(name_segment)

        self.logger.info(f'Segment "{name_segment}" is deleted')
        self.logger.info(f'Checking that the segment "{name_segment}" has been deleted')

        assert self.segments_page.element_not_present(elem_title)
