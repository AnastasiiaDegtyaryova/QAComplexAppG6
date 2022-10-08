import pytest

from pages.utils import Post


# class TestCreatePostPage:
#     log = logging.getLogger("[CreatePostPage]")


#
# def test_create_post_page(self, hello_page):
#     """
#     - Pre-conditions:
#         - Sign Up/Sign In as an user
#     - Steps:
#         - Navigate to create Post Page
#         - Create Post
#         - Verify the result
#     """
#     # Navigate to create Post Page
#     create_post_page = hello_page.header.navigate_to_create_post_page()
#
#     # Create Post
#     post = Post()
#     post.fill_default()
#     create_post_page.create_post(post)
#
#     # Verify the result
#     create_post_page.verify_successfully_created()
#     create_post_page.verify_all_attributes(post)
#
#
# def test_sign_out(self, header):
#     header.sign_out()
#     # self.log.info


class TestProfilePage:

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    @pytest.fixture()
    def hello_page_2_user(self, start_page, random_user_2):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user_2)

    def test_followings(self, hello_page, random_user_2):
        """
         - Pre-conditions:
             - Sign up as a user (user1)
             - Create a post
             - Sign Out
             - Sign Up as the other user (user2)
         - Steps:
             - Search  for post by user1
             - Navigate to post
             - Navigate to the user profile
             - Follow the user
             - Navigate to user2 profile
             - Verify following tab
         """

        # Navigate to create Post Page
        create_post_page = hello_page.header.navigate_to_create_post_page()

        # Create Post
        post = Post()
        post.fill_default()
        create_post_page.create_post(post)

        # Verify the result
        create_post_page.verify_successfully_created()
        create_post_page.verify_all_attributes(post)

        # Sign Out
        start_page = hello_page.header.sign_out()
        hello_page = start_page.sign_up_and_verify(random_user_2)
        hello_page.header.search_post(post.title)

        # Search for post by user1
