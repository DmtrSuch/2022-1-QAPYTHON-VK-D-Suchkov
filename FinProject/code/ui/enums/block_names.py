from enum import Enum
from code.ui.locators.MainPage_locators import MainPageLocators

class BlockLinkNames(Enum):
    API = 1,
    INTERNET = 2,
    SMTP = 3,

class ListBlockLinkLocators:
    Items = {
        BlockLinkNames.API: MainPageLocators.API_IMAGE,
        BlockLinkNames.INTERNET: MainPageLocators.INTERNET_IMAGE,
        BlockLinkNames.SMTP: MainPageLocators.SMPT_IMAGE
    }

class ListBLockLinkURL:
    Items = {
        "https://en.wikipedia.org/wiki/API": BlockLinkNames.API,
        "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/": BlockLinkNames.INTERNET,
        "https://ru.wikipedia.org/wiki/SMTP": BlockLinkNames.SMTP
    }
