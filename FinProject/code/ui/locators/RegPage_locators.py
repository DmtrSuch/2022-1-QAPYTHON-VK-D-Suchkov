from selenium.webdriver.common.by import By


class RegPageLocators():
    NAME_INPUT_LOCATOR = (By.ID, "user_name")
    SURNAME_INPUT_LOCATOR = (By.ID, "user_surname")
    MIDDLENAME_INPUT_LOCATOR = (By.ID, "user_middle_name")
    USERNAME_INPUT_LOCATOR = (By.ID, "username")
    EMAIL_INPUT_LOCATOR = (By.ID, "email")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT_LOCATOR = (By.ID, "confirm")
    CONFIRM_CHECKBOX_LOCATOR = (By.XPATH, "//input[@id = 'term']")
    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    ALLERT_LOCATOR = (By.XPATH, "//div[contains(@class, 'uk-alert')]")
    LOGIN_LOCATOR = (By.XPATH, '//a[@href="/login"]')
