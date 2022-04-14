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
        elem_title = self.find(
            (By.XPATH, self.locators.TITLE_NEW_SEGMENT_LOCATOR.format(name_segment)))
        assert elem_title.get_attribute('text') == name_segment

    @allure.step('Delete segment')
    def delete_segment(self, name_segment):
        elem_title = self.find((By.XPATH, self.locators.TITLE_NEW_SEGMENT_LOCATOR.format(name_segment)))
        id_segment = elem_title.get_attribute('href').split('/')[-1]

        self.click((By.XPATH, self.locators.DELETE_SEGMENT_CROSS_LOCATOR.format(id_segment)))

        self.click(self.locators.DELETE_SEGMENT_BUTTON_LOCATOR)
