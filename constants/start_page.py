class StartPageConstants:
    # Sign In
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / password"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_USERNAME_ERROR_XPATH = ".//*[contains(text(),'Username must be at least 3 characters.')]"
    SIGN_UP_USERNAME_ERROR_TEXT = "Username must be at least 3 characters."
    SIGN_UP_EMAIL_ERROR_XPATH = ".//*[contains(text(),'You must provide a valid email address.')]"
    SIGN_UP_EMAIL_ERROR_TEXT = ".//*[contains(text(),'You must provide a valid email address.')]"
    SIGN_UP_PASSWORD_ERROR_XPATH = ".//*[contains(text(),'Password must be at least 12 characters.')]"
    SIGN_UP_PASSWORD_ERROR_TEXT = "Password must be at least 12 characters."

    # TODO: this is actually next page
    HELLO_MESSAGE_XPATH = ".//h2"
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"
    HELLO_MESSAGE_TEXT = "Hello {username}, your feed is empty."
