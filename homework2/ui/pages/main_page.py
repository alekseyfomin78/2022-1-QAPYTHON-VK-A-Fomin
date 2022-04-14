import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = basic_locators.MainPageLocators()

    @allure.step('Go to Segments page')
    def go_to_segments(self):
        from ui.pages.segments_page import SegmentsPage
        self.driver.get('https://target.my.com/segments/segments_list')
        return SegmentsPage(self.driver)
