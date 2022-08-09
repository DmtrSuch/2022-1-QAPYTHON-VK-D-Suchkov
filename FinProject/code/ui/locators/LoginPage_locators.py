from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_INPUT_LOCATOR = (By.XPATH, '//input[contains(@placeholder, "Username")]')
    PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[contains(@placeholder, "Password")]')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//input[@type="submit"]')
    REG_BUTTON_LOCATOR = (By.XPATH, '//a[starts-with(@href, "/reg")]')
    WARNING_USERNAME_OR_PASSWORD_LOCATOR = (By.XPATH, "//div[contains(text(), 'Invalid username or password')]")
    WARNING_ACC_BLOCK = (By.XPATH, "//div[@id='flash']")