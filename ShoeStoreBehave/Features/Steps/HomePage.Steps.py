import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.homePage import HomePage
from Pages.navbarValidation import navBar
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig
import time


baseURL = ReadConfig.getURL()
myLogger = LogGen.loggen()

@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.chrome(ChromeDriverManager.install())
    myLogger.info("****Driver Initialized****")
    context.driver.get(baseURL)
    myLogger.info("****Browser Launched****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Welcome to Shoe Store Homepage!"
    if actual_title == expected_title:
        assert True
        context.driver.save.screenshot(".\\ScreenShots\\"+"HomePage.png")
        allure.attach(context.driver.get_screenshot_as_png(),name="ShoeStore Page test",attachment_type=AttachmentType.PNG)
        myLogger.info("****Title Matched!****")
    else:
        myLogger.info("****Title not Matched!****")
        context.driver.save.screenshot(".\\ScreenShots\\"+"HomePage.png")
        allure.attach(context.driver.get_screenshot_as_png(),name="ShoeStore Page test",attachment_type=AttachmentType.PNG)
        assert False
        time.sleep(5)


@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    myLogger.info("****Browser Closed!****")
