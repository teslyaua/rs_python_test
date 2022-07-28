class ChooseVideoComponent:
    UPLOAD_VIDEO_INPUT = '//button[contains(@class,"VideoFileUploadActions")]/preceding-sibling::input'
    CLOSE_BTN = '//button[contains(@class,"buttonClose")]'

    def __init__(self, page):
        self.page = page

    def upload_video(self, video_location):
        self.page.locator(self.UPLOAD_VIDEO_INPUT).set_input_files(video_location)
        self.page.wait_for_load_state('networkidle')
        return self

    def close_modal(self):
        self.page.locator(self.CLOSE_BTN).click()
