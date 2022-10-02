from selenium.webdriver.common.keys import Keys

from constants.chat import ChatPageConstants
from pages.base_page import BasePage


class ChatPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatPageConstants()

    def send_message(self, message):
        """Send message"""
        self.fill_field(xpath=self.constants.CHAT_INPUT_XPATH, value=message + Keys.ENTER)

    def verify_sent_message(self, message):
        """Verify success message"""
        assert self.get_element_text(xpath=self.constants.CHAT_MESSAGE_XPATH) == message, \
            f"Actual: {self.get_element_text(xpath=self.constants.CHAT_MESSAGE_XPATH)}"
