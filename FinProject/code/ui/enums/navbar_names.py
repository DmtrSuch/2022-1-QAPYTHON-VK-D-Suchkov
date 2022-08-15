from enum import Enum
from code.ui.locators.MainPage_locators import MainPageLocators
from code.config.creds import APP_PORT, APP_SERVICE


class NavbarLinkNames(Enum):
    HOME = 1,
    HOME_2 = 2,
    PYTHON = 3,
    PYTHON_HISTORY = 4,
    FLASK = 5,
    CENTOS = 6,
    WIRESHARK_NEWS = 7,
    WIRESHARK_DOWNLOAD = 8,
    TCPDUMP_EXAMPLES = 9,

class NavbarLinkListButtonLocator:
    Items = {
        NavbarLinkNames.PYTHON_HISTORY: MainPageLocators.PYTHON_BUTTON,
        NavbarLinkNames.FLASK: MainPageLocators.PYTHON_BUTTON,
        NavbarLinkNames.CENTOS: MainPageLocators.LINUX_BUTTON,
        NavbarLinkNames.WIRESHARK_NEWS: MainPageLocators.NETWORK_BUTTON,
        NavbarLinkNames.WIRESHARK_DOWNLOAD: MainPageLocators.NETWORK_BUTTON,
        NavbarLinkNames.TCPDUMP_EXAMPLES: MainPageLocators.NETWORK_BUTTON,
    }

class NavbarLinkButtonLocator:
    Items = {
        NavbarLinkNames.HOME: MainPageLocators.HOME_LINK,
        NavbarLinkNames.HOME_2: MainPageLocators.HOME_LINK_2,
        NavbarLinkNames.PYTHON: MainPageLocators.PYTHON_LINK,
        NavbarLinkNames.PYTHON_HISTORY: MainPageLocators.PYTHON_HISTORY_LINK,
        NavbarLinkNames.FLASK: MainPageLocators.ABOUT_FLASK_LINK,
        NavbarLinkNames.CENTOS: MainPageLocators.DOWNLOAD_CENTOS_LINK,
        NavbarLinkNames.WIRESHARK_NEWS: MainPageLocators.NETWORK_WIRESHARK_NEWS_LINK,
        NavbarLinkNames.WIRESHARK_DOWNLOAD: MainPageLocators.NETWORK_WIRESHARK_DOWNLOAD_LINK,
        NavbarLinkNames.TCPDUMP_EXAMPLES: MainPageLocators.NETWORK_TCPDUMP_EXAMPLES_LINK,
    }

class NavbarLinkUrl:
    Items = {
        f"http://{APP_SERVICE}:{APP_PORT}/welcome/": NavbarLinkNames.HOME,
        "https://www.python.org/": NavbarLinkNames.PYTHON,
        "https://en.wikipedia.org/wiki/History_of_Python": NavbarLinkNames.PYTHON_HISTORY,
        "https://flask.palletsprojects.com/en/1.1.x/#": NavbarLinkNames.FLASK,
        "https://getfedora.org/ru/workstation/download/": NavbarLinkNames.CENTOS,
        "https://www.wireshark.org/news/":  NavbarLinkNames.WIRESHARK_NEWS,
        "https://www.wireshark.org/#download":NavbarLinkNames.WIRESHARK_DOWNLOAD,
        "https://hackertarget.com/tcpdump-examples/": NavbarLinkNames.TCPDUMP_EXAMPLES
    }