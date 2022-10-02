# Дописати асерт, локатор на пароль
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
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_incorrect_password(self):
        """
        - Pre-conditions:
            - Create driver
            - Open page
        - Steps:
            - Fill login with valid data
            - Fill password with valid data
            - Click button
            - Verify error
        - Post-conditions:
            - Close driver
        """
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\nepoc\PycharmProjects\QaComplexAppG6\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open start page")

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("tester")
        sleep(1)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value="дописати")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        # error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        # assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()
