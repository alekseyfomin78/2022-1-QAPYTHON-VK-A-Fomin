from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.dashboard_page import DashboardPage


class ErrorLoginException(Exception):
    pass


class LoginPage(BasePage):
    locators = basic_locators.LoginPageLocators()
    url = 'https://target.my.com/'

    def login(self, email, password) -> DashboardPage:
        self.click(self.locators.LOGIN_LOCATOR)

        elem_email = self.find(self.locators.EMAIL_LOCATOR)
        elem_email.clear()
        elem_email.send_keys(email)

        elem_password = self.find(self.locators.PASSWORD_LOCATOR)
        elem_password.clear()
        elem_password.send_keys(password)

        self.click(self.locators.AUTH_BUTTON_LOCATOR)
        if self.driver.current_url == 'https://target.my.com/dashboard':
            return DashboardPage(self.driver)

        # проверка перехода на страницу account.my и на уведомление о неверном логине или пароле
        if (self.driver.current_url == f'https://account.my.com/login/?error_code=1&email={email}&continue'
                                       f'=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526'
                                       f'ignore_opener%253D1%23email' or
                self.find(basic_locators.LoginPageLocators.ERROR_LOGIN_MESSAGE)):
            raise ErrorLoginException(f'Invalid login: {email} or password: {password}')


