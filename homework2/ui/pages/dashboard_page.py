import allure

from ui.locators import basic_locators
from ui.pages.main_page import MainPage


class DashboardPage(MainPage):
    locators = basic_locators.DashboardPageLocators()
    url = 'https://target.my.com/dashboard'

    @allure.step('Create new advertisement campaign')
    def create_ad_campaign(self, image_file_path, url_of_the_advertised_object, campaign_name):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)

        self.find(self.locators.LOAD_CONTENT_PAGE_LOCATOR)

        self.click(self.locators.TRAFFIC_LOCATOR)

        field_for_url = self.find(self.locators.FIELD_FOR_URL_LOCATOR)
        field_for_url.clear()
        field_for_url.send_keys(url_of_the_advertised_object)

        self.find(self.locators.LOAD_CONTENT_CAMPAIGN_NAME_LOCATOR)

        field_for_campaign_name = self.find(self.locators.FIELD_FOR_CAMPAIGN_NAME_LOCATOR)
        self.scroll(field_for_campaign_name)
        field_for_campaign_name.clear()
        field_for_campaign_name.send_keys(campaign_name)

        elem_teaser = self.find(self.locators.TEASER_LOCATOR)
        self.scroll(elem_teaser)
        elem_teaser.click()

        self.find(self.locators.LOAD_CONTENT_TEASER_LOCATOR)

        elem_upload_image = self.find(self.locators.UPLOAD_IMAGE_LOCATOR)
        self.scroll(elem_upload_image)

        button_upload_image = self.find(self.locators.UPLOAD_IMAGE_BUTTON_LOCATOR)
        button_upload_image.send_keys(image_file_path)

        elem_ad_title = self.find(self.locators.FIELD_FOR_AD_TITLE_LOCATOR)
        self.scroll(elem_ad_title)
        elem_ad_title.clear()
        elem_ad_title.send_keys(campaign_name)

        elem_ad_text = self.find(self.locators.FIELD_FOR_AD_TEXT_LOCATOR)
        self.scroll(elem_ad_text)
        elem_ad_text.clear()
        elem_ad_text.send_keys(campaign_name)

        self.click(self.locators.SAVE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)

