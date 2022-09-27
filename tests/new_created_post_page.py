# Доробити
import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestNewCreatedPostPage:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture()
    def hello_page(self, start_page):
        """Sign Up as the user and return the page"""
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        return start_page.sign_up_and_verify(username_value, email_value, password_value)

    def test_create_post_page(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Navigate to create Post Page
            - Create Post
            - Verify the result
        """
        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()
        self.log.info("Moved to Create Post Page")

        # Create Post
        create_post_page.create_post(title=random_str(15), body=random_str(150))
        self.log.info("Post created")

        # Verify the result
        create_post_page.verify_successfully_created()
        self.log.info("Message was verified")

    @pytest.fixture()
    def create_post(self, hello_page):
        """Create post and return the page"""
        create_post_page = hello_page.header.navigate_to_create_post_page()
        create_post_page.create_post(title=random_str(15), body=random_str(150))
        return create_post_page.verify_successfully_created()

    def test_edit_post_page(self, new_created_post_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
            - Post created
        - Steps:
            - Edit post title
            - Edit post body
            - Verify the result

        """
        # # Navigate to create Post Page
        # create_post_page = hello_page.header.navigate_to_create_post_page()
        # self.log.info("Moved to Create Post Page")
        #
        # # Create Post
        # create_post_page.create_post(title=random_str(15), body=random_str(150))
        # self.log.info("Post created")

        new_created_post_page.edit_post(title=random_str(15), body=random_str(150))
        self.log.info("Post updated")

        # Verify the result
        new_created_post_page.verify_successfully_edited()
        self.log.info("Message was verified")

    @pytest.fixture()
    def create_post(self, hello_page):
        """Create post and return the page"""
        create_post_page = hello_page.header.navigate_to_create_post_page()
        create_post_page.create_post(title=random_str(15), body=random_str(150))
        return create_post_page.verify_successfully_created()

    def test_trash_post_page(self, new_created_post_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
            - Post created
        - Steps:
            - Trash post
            - Verify the result

        """
        new_created_post_page.trash_post()
        self.log.info("Post deleted")

        # Verify the result
        new_created_post_page.verify_successfully_trashed()
        self.log.info("Message was verified")
