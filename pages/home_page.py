import logging

import allure

from components.account_item import AccountItemComponent
from components.video_modal import ChooseVideoComponent

logger = logging.getLogger()


class HomePage:
    URL = '/home'

    UPLOAD_VIDEO = 'text=Upload & Stream a Video File'

    def __init__(self, page):
        self.page = page
        self.video_modal = ChooseVideoComponent(self.page)

    @allure.step('Navigate to Login Page')
    def navigate(self):
        self.page.goto(self.URL)
        logger.info('Current Url = ' + self.page.url)
        return self

    @allure.step('Open Upload & Stream a Video File modal')
    def open_upload_video_modal(self):
        self.page.locator(self.UPLOAD_VIDEO).click()
        return self.video_modal
