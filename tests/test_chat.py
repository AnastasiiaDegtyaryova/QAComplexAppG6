import logging

import pytest


class TestChatPage:
    log = logging.getLogger("[TestChatPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_create_message(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Click on Chat button
            - Type message
            - Send message
        """
        # Send Message
        send_message = hello_page.header.open_chat_page()
        # Type message
        from pages.utils import random_str
        sent_random_message = random_str(25)
        send_message.send_message(sent_random_message)
        # Verify the result
        send_message.verify_sent_message(message=sent_random_message)
        self.log.info("Message:")
        from time import sleep
        sleep(10)
