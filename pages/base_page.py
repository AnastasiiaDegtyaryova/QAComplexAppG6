import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        return self.waiter.until(method=expected_conditions.visiility_of_element_locted((By.XPATH, xpath)))

    # Перевірка наявності елемента в дереві
    def is_exists(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """Clear and fill field"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def get_element_text(self, xpath):
        """Find element and get text"""
        # Verify error
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text
        # assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element}"
