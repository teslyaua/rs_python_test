import logging

import allure

from components.account_item import AccountItemComponent

logger = logging.getLogger()


class LoginPage:
    URL = '/login'

    EMAIL_FIELD = '#email'
    PASSWORD_FIELD = '#password'
    LOG_IN_BUTTON = '#submit'

    def __init__(self, page):
        self.page = page
        self.account_item = AccountItemComponent(self.page)

    @allure.step('Navigate to Login Page')
    def navigate(self):
        self.page.goto(self.URL)
        logger.info('Current Url = ' + self.page.url)
        return self

    def login_to_system(self, user_email, user_pswd):
        with allure.step(f'Log in with user: {user_email}'):
            logger.debug(f'Log in with user: {user_email}')
            self.page.locator(self.EMAIL_FIELD).fill(user_email)
            self.page.locator(self.PASSWORD_FIELD).fill(user_pswd)
            self.page.locator(self.LOG_IN_BUTTON).click()
            self.page.wait_for_url(f'**/home')
