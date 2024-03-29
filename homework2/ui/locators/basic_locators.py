from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGOUT_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/logout"]')

    BILLING_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
    STATISTICS_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
    SEGMENTS_LOCATOR = (By.XPATH, '//a[@href="/segments"]')


class LoginPageLocators(BasePageLocators):
    LOGIN_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    AUTH_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    ERROR_LOGIN_MESSAGE = (By.XPATH, '//div[contains(@class, "notify-module-content")]')


class ProfilePageLocators(BasePageLocators):
    PROFILE_CONTACTS_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    FULL_NAME_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//child::input')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//child::input')
    SAVE_CONTACTS_BUTTON_LOCATOR = (By.CLASS_NAME, 'button__text')


class DashboardPageLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "button-module-textWrapper")]')
    LOAD_CONTENT_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "js-target-content")]')
    TRAFFIC_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    FIELD_FOR_URL_LOCATOR = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    LOAD_CONTENT_CAMPAIGN_NAME_LOCATOR = (By.XPATH, '//div[@class="base-settings__campaign-name-wrap '
                                                    'js-base-setting-campaign-name-wrap"]')
    FIELD_FOR_CAMPAIGN_NAME_LOCATOR = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//child::input')
    TEASER_LOCATOR = (By.XPATH, '//div[contains(@id, "patterns_teaser")]')
    LOAD_CONTENT_TEASER_LOCATOR = (By.XPATH, '//div[contains(@class, "campaign__after-wrap")]')
    UPLOAD_IMAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "roles-module-buttonWrap")]')
    UPLOAD_IMAGE_BUTTON_LOCATOR = (By.XPATH, '//input[contains(@data-test, "image_90x75")]')
    FIELD_FOR_AD_TITLE_LOCATOR = (By.XPATH, '//input[contains(@data-name, "title")]')
    FIELD_FOR_AD_TEXT_LOCATOR = (By.XPATH, '//textarea[contains(@data-name, "text")]')
    SAVE_CAMPAIGN_BUTTON_LOCATOR = (By.XPATH, '//button[@data-service-readonly="true"]')
    MESSAGE_ABOUT_SUCCESSFUL_CREATION = (By.XPATH, '//div[contains(@class, "notify-module-content")]')
    CHECK_TITLE_CAMPAIGN_LOCATOR = '//a[@title="{}"]'


class SegmentsPageLocators(BasePageLocators):
    CREATE_NEW_SEGMENT_LOCATORS = (By.XPATH, '//div[contains(@class, "js-create-button-wrap")]')
    CHECKBOX_LOCATOR = (By.XPATH, '//input[@type="checkbox"]')
    ADD_SEGMENT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "js-add-button")]//child::button')
    FIELD_FOR_NAME_NEW_SEGMENT_LOCATORS = (By.XPATH, '//div[contains(@class, '
                                                     '"input_create-segment-form")]//child::input')
    CREATE_NEW_SEGMENT_BUTTON_LOCATORS = (By.XPATH, '//button[contains(@class, "button_submit")]')
    APP_AND_GAME_LOCATOR = (By.XPATH, '//div[@class="adding-segments-item"]')
    DELETE_SEGMENT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
    TITLE_NEW_SEGMENT_LOCATOR = '//a[@title="{}"]'
    DELETE_SEGMENT_CROSS_LOCATOR = '//div[contains(@data-test, "remove-{}")]//child::span'
