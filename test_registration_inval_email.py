import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=1):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_register(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill username field with valid data
            - Fill email with invalid data
            - Fill password fields with valid data
            - Click on Sign Up button
            - Verify error text
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\nepoc\PycharmProjects\QaComplexAppG6\chromedriver.exe")

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info("Open start page")

        # Fill username
        user = self.random_str()
        username_value = f"{user}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{user}{self.random_num()}mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click on Sign Up button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("User was registered")
        sleep(1)

        # Verify Error text

        assert driver.find_element(by=By.XPATH,
                                   value=".//*[contains(text(),'You must provide a valid email address.')]").text == 'You must provide a valid email address.'
        self.log.info("Registration for user '%s' was  not success and verified", username_value)
