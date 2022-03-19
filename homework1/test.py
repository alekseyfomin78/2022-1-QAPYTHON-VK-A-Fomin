import pytest
from base import BaseCase, get_random_info
from ui import locators


class Test(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_change_profile_contacts(self):
        name = get_random_info(100)
        phone = get_random_info(20)

        self.login()

        self.click(locators.PROFILE_CONTACTS_LOCATOR)

        full_name = self.find(locators.FULL_NAME_LOCATOR)
        full_name.clear()
        full_name.send_keys(name)

        phone_number = self.find(locators.PHONE_NUMBER_LOCATOR)
        phone_number.clear()
        phone_number.send_keys(phone)

        self.click(locators.SAVE_CONTACTS_BUTTON_LOCATOR)
        assert full_name.get_attribute('value') == name and phone_number.get_attribute('value') == phone

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "locator, url",
        [
            (locators.BILLING_LOCATOR, 'https://target.my.com/billing#deposit'),
            (locators.STATISTICS_LOCATOR, 'https://target.my.com/statistics/summary')
        ]
    )
    def test_change_page(self, locator, url):
        self.login()
        self.find(locator)
        self.click(locator)
        assert self.url_matches(url)
