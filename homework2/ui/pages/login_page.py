from ui.locators import basic_locators
from ui.pages.base_page import BasePage, PageNotOpenedExeption
from ui.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    locators = basic_locators.LoginPageLocators()
    url = 'https://target.my.com/'

    def login(self, email, password):
        self.click(self.locators.LOGIN_LOCATOR)

        elem_email = self.find(self.locators.EMAIL_LOCATOR)
        elem_email.clear()
        elem_email.send_keys(email)

        elem_password = self.find(self.locators.PASSWORD_LOCATOR)
        elem_password.clear()
        elem_password.send_keys(password)

        self.click(self.locators.AUTH_BUTTON_LOCATOR)
        # return DashboardPage(self.driver)


