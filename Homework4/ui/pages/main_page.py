from ui.pages.base_page import BasePage
from ui.pages.base_page import PageNotLoadedException
from ui.locators.locators_android import MainPageANDROIDLocators
import allure


RETRY = 3

class MainPage(BasePage):
    locators = MainPageANDROIDLocators()
    def use_keyboard(self):
        pass

    def search(self,text):
        pass

    def go_to_menu(self):
        pass

    def skip_notification(self):
        pass

class MainPageANDROID(MainPage):
    locators = MainPageANDROIDLocators()

    @allure.step("Пропускаем уведомления")
    def skip_notification(self):
        if self.driver.desired_capabilities['autoGrantPermissions'] == False:
            self.click_for_android(self.locators.SKIP_LOCATOR)
            self.click_for_android(self.locators.SKIP_LOCATOR)
        else:
            pass

    @allure.step("Пропускаем уведомления")
    def go_to_menu(self):
        self.click_for_android(self.locators.MENU_BUTTON_LOCATOR)

    @allure.step("Используем окно ввода")
    def use_keyboard(self):
        self.click_for_android(self.locators.KEYBORD_BUTTON)

    @allure.step("Ввод текста")
    def search(self,text):
        check =''
        if '+' in text:
            locator = ''
            for i in range(RETRY):
                try:
                    self.input_for_android(self.locators.INPUT_LOCATOR,text)
                    self.click_for_android(self.locators.INPUT_SEND_LOCATOR)
                    temp = text.split('+')
                    check = str(int(temp[0]) + int(temp[1]))
                    locator = self.locators.ANSWER_CALC_LOCATOR
                    if i == 0:
                        locator = self.locators.ANSWER_LOCATOR
                    if check in self.find(locator).text:
                        assert check == self.find(locator).text
                        return
                except PageNotLoadedException:
                    if i == RETRY - 1:
                        raise

            assert check == self.find(locator).text.lower()
        elif text == 'News':
                self.input_for_android(self.locators.INPUT_LOCATOR, text)
                self.click_for_android(self.locators.INPUT_SEND_LOCATOR)


        elif text == 'stop':
                self.input_for_android(self.locators.INPUT_LOCATOR, text)
                self.click_for_android(self.locators.INPUT_SEND_LOCATOR)
        else:
                for i in range(RETRY):
                    try:
                        self.input_for_android(self.locators.INPUT_LOCATOR, text)
                        self.click_for_android(self.locators.INPUT_SEND_LOCATOR)
                        check = ['ещё', 'еще']
                        if check[0] in self.find(self.locators.ANSWER_LOCATOR).text.lower():
                            assert check[0] in self.find(self.locators.ANSWER_LOCATOR).text.lower()
                            return
                        if check[1] in self.find(self.locators.ANSWER_LOCATOR).text.lower():
                            assert check[1] in self.find(self.locators.ANSWER_LOCATOR).text.lower()
                            return
                    except PageNotLoadedException:
                        if i == RETRY - 1:
                            raise
