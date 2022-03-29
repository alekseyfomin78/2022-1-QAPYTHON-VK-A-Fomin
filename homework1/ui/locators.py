from selenium.webdriver.common.by import By


LOGIN_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
EMAIL_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
AUTH_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')

LOGOUT_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/logout"]')

PROFILE_CONTACTS_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
FULL_NAME_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//child::input')
PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//child::input')
SAVE_CONTACTS_BUTTON_LOCATOR = (By.CLASS_NAME, 'button__text')

BILLING_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
STATISTICS_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')

