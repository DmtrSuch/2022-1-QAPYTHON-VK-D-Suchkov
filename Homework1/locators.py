from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "responseHead-module-button")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "authForm-module-button")]')
    BASEPAGE_BIGTITLE_LOCATOR = (By.XPATH, '//*[contains(@class, "mainPage-module-bigTitle")]')


class MainPageLocators(BasePageLocators):
    SCROLL_MENU_LOCATOR = (By.XPATH, '//*[contains(@class, "right-module-rightButton")]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//*[@href="/logout"]')
    INSTRUCTION_MODULE_TITLE_LOCATOR = (By.XPATH, '//*[contains(@class, "instruction-module-title")]')
    PROFILE_LOCATOR = (By.XPATH, '//*[@href="/profile"]')
    TOOLS_LOCATOR = (By.XPATH, '//*[@href="/tools"]')
    BILLING_LOCATOR = (By.XPATH, '//*[@href="/billing"]')


class ProfilePageLocators(MainPageLocators):
    FULLNAME_INFO_LOCATOR = (By.XPATH, '//*[contains(@class, "input__inp")]')
    NUMBER_INFO_LOCATOR = (By.XPATH, '//*[contains(@data-name, "phone")]/div/input')
    SAVE_INFO_LOCATOR = (By.XPATH, '//*[contains(@class, "button button_submit")]')
    SUCCESSSAVE_LOCATOR = (By.XPATH, '//*[contains(@data-class-name, "SuccessView")]/div')


class ToolsPageLocators(MainPageLocators):
    TOOLS_FEEDS_LOCATOR = (By.XPATH, '//*[contains(@class, "feeds-module-title")]')


class BillingPageLocators(MainPageLocators):
    SUBTITLE_BILLING_LOCATOR = (By.XPATH, '//*[contains(@class, "deposit__payment-form__subtitle")]')
