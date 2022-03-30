from selenium.webdriver.common.by import By


class BasePageLocators:
    pass

class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "responseHead-module-button")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "authForm-module-button")]')
    BASEPAGE_BIGTITLE_LOCATOR = (By.XPATH, '//*[contains(@class, "mainPage-module-bigTitle")]')


class MainPageLocators:
    SCROLL_MENU_LOCATOR = (By.XPATH, '//*[contains(@class, "right-module-rightButton")]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//*[@href="/logout"]')
    CREATE_COMPANY_LOCATOR = (By.XPATH,'//*[contains(@class,"dashboard-module-createButtonWrap")]/div/div')
    CHECK_MP_LOCATOR = (By.XPATH,'//*[contains(@class,"header-module")]')
    SEGMENT_LOCATOR =(By.XPATH,'//*[@href="/segments"]')



class CompanyPageLocator:
    TRAFFIC_LOCATOR = (By.XPATH,'//*[contains(@class,"column-list-item _traffic")]/div')
    REFERENCE_LOCATOR = (By.XPATH, '//*[contains(@class,"suggester-module-wrapper")]/div/input')
    NAME_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class,"input input_campaign-name")]/div/input')
    BANNER_COMPANY_LOCATOR =(By.XPATH, '//*[contains(@id, "patterns_banner_4")]')
    BANNERS_CMP_LOCATOR=(By.XPATH, '//*[contains(@class, "banners")]')
    CLICK_ROLES_LOCATOR = (By.XPATH,'//*[contains(@class, "imagePreview - module - emptyImageText")]')
    ROLES_LOCATOR = (By.XPATH,'//*[contains(@data-pattern-id, "4")]/div/div/input')
    SAVE_COMPANY_LOCATOR = (By.XPATH, '//*[contains(@class, "footer")]/div/div/button/div')



class SegmentsPageLocator:
    CREATE_LOCATOR = (By.XPATH, '//*[contains(@class, "button__text")]')
    CID_LOCATOR = (By.XPATH, '//*[contains(@cid, "view392")]')
    CHECK_BOX_LOCATOR = (By.XPATH, '//*[contains(@class, "adding-segments-source__checkbox")]')
    NAME_SEGMENT = (By.XPATH, '//*[contains(@class, "adding-segments-source__checkbox")]/div/div/input')
    BUTTON_LOCATOR = (By.XPATH, '//*[contains(@class, "button__text")]')