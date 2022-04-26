from selenium import webdriver
import os


def capability_select(device_os):
    capability = None
    if device_os == 'android':
        capability = {"platformName": "Android",
                      "platformVersion": "8.1",
                      "automationName": "Appium",
                      "appPackage": "ru.mail.search.electroscope",
                      "appActivity": ".ui.activity.AssistantActivity",
                      "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                          '../stuff/Marussia_v1.57.0.apk')
                                             ),
                      "orientation": "PORTRAIT",
                      "autoGrantPermissions": "true"
                      }
    else:
        raise ValueError("Incorrect device os type")
    return capability
