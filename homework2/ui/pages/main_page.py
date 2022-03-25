from selenium.common.exceptions import StaleElementReferenceException
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = basic_locators.MainPageLocators()

    def go_to_segments(self):
        from ui.pages.segments_page import SegmentsPage
        try:
            self.click(self.locators.SEGMENTS_LOCATOR)
        except StaleElementReferenceException:
            self.click(self.locators.SEGMENTS_LOCATOR)
        return SegmentsPage(self.driver)
