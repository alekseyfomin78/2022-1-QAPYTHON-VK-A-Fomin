import pytest
from ui import locators
import credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
import random
import string


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        ignored_exceptions = (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException)
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout, ignored_exceptions=ignored_exceptions, poll_frequency=3)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=15):
        self.find(locator, timeout=timeout)
        self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def login(self):
        email = credentials.email
        password = credentials.password

        self.click(locators.LOGIN_LOCATOR)

        elem_email = self.find(locators.EMAIL_LOCATOR)
        elem_email.clear()
        elem_email.send_keys(email)

        elem_password = self.find(locators.PASSWORD_LOCATOR)
        elem_password.clear()
        elem_password.send_keys(password)

        self.click(locators.AUTH_BUTTON_LOCATOR)

    def logout(self):
        self.click(locators.LOGOUT_LOCATOR)
        try:
            self.click(locators.LOGOUT_BUTTON_LOCATOR)
        except ElementClickInterceptedException:
            self.click(locators.LOGOUT_BUTTON_LOCATOR)

    def url_matches(self, url, timeout=None):
        return self.wait(timeout).until(EC.url_matches(url))


def get_random_info(max_length):
    return ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(random.randint(1,
                                                                                                           max_length)))
