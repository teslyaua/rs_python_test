import logging

import allure
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage

logger = logging.getLogger()


class Application:

    def __init__(self, page: Page):
        self.page = page

    @allure.step('[Application] Navigate to page: {2}')
    def goto(self, link, page_name=''):
        logger.info(f'Navigating to {page_name} with url: {link}')
        self.page.goto(link, timeout=30000)

    @property
    def login_page(self):
        return LoginPage(self.page)

    @property
    def home_page(self):
        return HomePage(self.page)
