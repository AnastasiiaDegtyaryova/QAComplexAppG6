from time import sleep

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\nepoc\PycharmProjects\QaComplexAppG6\chromedriver.exe")


@pytest.fixture(scope="class")
def reg_form():
    print("Before")
    yield RegistrationForm()
    print("After")


@pytest.fixture(scope="function")
def set_username(reg_form):
    reg_form.username = "testusername1"
    yield
    reg_form.username = reg_form.username + "1"


@pytest.fixture(scope="function")
def set_email(reg_form):
    reg_form.email = "testemail1@gmail.com"
    yield
    reg_form.email = "1" + reg_form.email


@pytest.fixture(scope="function")
def set_password(reg_form):
    reg_form.password = "testpassword1"
    yield
    reg_form.password = reg_form.password + "1"


def test_default(set_username, set_email, set_password):
    # Open page
    driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

    # Fill username
    username = driver.find_element(by=By.XPATH, value=".//*[@id='username-register']")
    username.send_keys("user00000")
    sleep(1)

    # Fill email
    email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
    email.send_keys("email00000@gmail.com")
    sleep(1)

    # Fill password
    password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
    password.send_keys("password12456700")
    sleep(1)

    # Click button
    button = driver.find_element(by=By.XPATH, value=".//button[contains(text(),'Sign up for OurApp')]")
    button.click()
    sleep(1)

    # Check user is registered

    required_element = driver.find_element(by=By.XPATH, value=".//a[contains(text(),'Create Post')]")
    assert required_element.text == "Create Post", f"Actual message: {required_element.text}"

    # Close driver
    driver.close()


class RegistrationForm:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
