import os
import random
import string

import allure
import pytest
from ui.pages.login_page import LoginPage


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.login_page: LoginPage = request.getfixturevalue('login_page')

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, temp_dir):
        yield
        browser_logs = os.path.join(temp_dir, 'browser.log')
        with open(browser_logs, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

        with open(browser_logs, 'r') as f:
            allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)

        allure.attach.file(os.path.join(temp_dir, 'test.log'), 'test.log', allure.attachment_type.TEXT)

        screenshot_path = os.path.join(temp_dir, 'screenshot.png')
        driver.get_screenshot_as_file(screenshot_path)
        allure.attach.file(screenshot_path, 'screenshot.png', allure.attachment_type.PNG)

    @pytest.fixture(scope='function', autouse=True)
    def authorization(self, driver, credentials, request):
        if self.authorize:
            self.login_page = request.getfixturevalue('login_page')
            self.login_page.login(*credentials)
            self.dashboard_page = request.getfixturevalue('dashboard_page')
            return self.dashboard_page


def get_random_info(max_length):
    return ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(random.randint(1,
                                                                                                           max_length)))
