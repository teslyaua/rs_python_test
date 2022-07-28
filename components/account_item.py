class AccountItemComponent:
    ACCOUNT_TITLE = '//span[contains(@class,"account-item-button_title")]'

    def __init__(self, page):
        self.page = page

    def get_account_name(self):
        return self.page.locator(self.ACCOUNT_TITLE).inner_text()
