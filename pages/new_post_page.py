from constants.new_post_page import NewPostConstants
from pages.base_page import BasePage


class NewPost(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = NewPostConstants()
        from pages.header import Header
        self.header = Header(self.driver)

    def edit_post(self, title, body):
        """Edit post using provided values"""
        self.click(xpath=self.constants.EDIT_POST_BUTTON_XPATH)
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    def verify_successfully_edited(self):
        """Verify success message editing"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_UPDATE_MESSAGE_XPATH) == self.constants.SUCCESS_UPDATE_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_UPDATE_MESSAGE_XPATH)}"

    def trash_post(self):
        """Edit post using provided values"""
        self.click(xpath=self.constants.TRASH_POST_BUTTON_XPATH)

    def verify_successfully_trashed(self):
        """Verify success message editing"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_TRASH_MESSAGE_XPATH) == self.constants.SUCCESS_TRASH_MESSAGE_TEXT, \
            f"Actual: {self.get_element_text(xpath=self.constants.SUCCESS_TRASH_MESSAGE_XPATH)}"

