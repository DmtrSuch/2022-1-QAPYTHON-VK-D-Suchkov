from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass


class MainPageANDROIDLocators(BasePageANDROIDLocators):
    KEYBORD_BUTTON = (By.ID, 'ru.mail.search.electroscope:id/keyboard')
    SKIP_LOCATOR = (By.ID, 'com.android.packageinstaller:id/permission_deny_button')
    INPUT_LOCATOR = (By.ID, 'ru.mail.search.electroscope:id/input_text')
    INPUT_SEND_LOCATOR = (By.ID, 'ru.mail.search.electroscope:id/text_input_send')
    SWIPE_POPULATION = (By.XPATH,'//android.view.ViewGroup[4]/android.widget.TextView')
    SWIPE_CLICK = (By.XPATH,'//android.view.ViewGroup[5]/android.widget.TextView')
    ANSWER_LOCATOR =(By.XPATH,'//androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    ANSWER_CALC_LOCATOR = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    BIG_ANSWER_LOCATOR = (By.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')
    MENU_BUTTON_LOCATOR = (By.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')
    TURN_NEWS1_LOCATION = (By.ID,'ru.mail.search.electroscope:id/player_track_duration')
    TURN_NEWS2_LOCATION = (By.ID,'ru.mail.search.electroscope:id/player_track_name')
    PLAY_NEWS_LOCATION = (By.ID,'ru.mail.search.electroscope:id/play_seek_bar')

class MenuPageANDROIDLocators(BasePageANDROIDLocators):
    SOURCE_NEWS_LOCATOR =(By.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    MAIL_NEWS_LOCATOR = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')
    BACK_NEWS_LOCATOR = (By.XPATH,'//android.widget.LinearLayout/android.widget.ImageButton')
    EXIT_MENU_LOCATOR =(By.XPATH,
    '//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout'
    '/android.widget.LinearLayout/android.widget.ImageButton')
    CHECK_MARK = (By.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')
    CHECK_VERSION_LOCATOR = (By.ID, 'ru.mail.search.electroscope:id/user_settings_about')
    VERSION_APP_LOCATOR =(By.ID,'ru.mail.search.electroscope:id/about_version')
    COPYRIGHT_LOCATOR =(By.ID,'ru.mail.search.electroscope:id/about_copyright')



