import allure
from selenium.webdriver.common.by import By

from ui.locators import basic_locators
from ui.pages.main_page import MainPage


class SegmentsPage(MainPage):
    locators = basic_locators.SegmentsPageLocators()
    url = 'https://target.my.com/segments/segments_list'

    @allure.step('Create new segment')
    def create_new_segment(self, name_segment):
        self.click(self.locators.CREATE_NEW_SEGMENT_LOCATORS)
        self.click(self.locators.APP_AND_GAME_LOCATOR)
        self.click(self.locators.CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR)
        elem_name_new_segment = self.find(self.locators.FIELD_FOR_NAME_NEW_SEGMENT_LOCATORS)
        elem_name_new_segment.clear()
        elem_name_new_segment.send_keys(name_segment)
        self.click(self.locators.CREATE_NEW_SEGMENT_BUTTON_LOCATORS)

    @allure.step('Delete segment')
    def delete_segment(self, name_segment):
        TITLE_NEW_SEGMENT_LOCATOR = (By.XPATH, f'//a[@title="{name_segment}"]')
        elem_title = self.find(TITLE_NEW_SEGMENT_LOCATOR)
        id_segment = elem_title.get_attribute('href').split('/')[-1]

        DELETE_SEGMENT_CROSS_LOCATOR = (By.XPATH, f'//div[contains(@data-test, "remove-{id_segment}")]//child::span')
        self.click(DELETE_SEGMENT_CROSS_LOCATOR)

        self.click(self.locators.DELETE_SEGMENT_BUTTON_LOCATOR)


