import time

import allure
from selenium.webdriver import ActionChains

from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = basic_locators.BasePageLocators()
    url = 'https://target.my.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 30
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Find element')
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Click element')
    def click(self, locator, timeout=None):
        self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def scroll(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def url_matches(self, url, timeout=None):
        return self.wait(timeout).until(EC.url_matches(url))

    def element_not_present(self, element, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element(element))
