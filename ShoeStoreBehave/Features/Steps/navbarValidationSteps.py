import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.homePage import HomePage
from Pages.navbarValidation import myLogger, baseURL, navBar


@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.chrome(ChromeDriverManager.install())
    myLogger.info("****Driver Initialized ****")
    context.driver.get(baseURL)
    myLogger.info("****Browser Launched ****")


@when(u'navbar element found')
def step_impl(context):
    myLogger.info("****Navbar Element Found ****")
    global hpage
    global nbar
    hpage = HomePage(context.driver)
    hpage.titleDisplayed()
    time.sleep(5)
    nbar = navBar(context.driver)
    nbar.clickonAllShoes()
    myLogger.info("****Navbar Element Found! ****")




@then(u'navigate to All Shoes')
def step_impl(context):
    myLogger.info("****Navbar Element Found ****")
    global hpage
    global nbar
    hpage = HomePage(context.driver)
    hpage.titleDisplayed()
    time.sleep(5)
    nbar = navBar(context.driver)
    nbar.clickonAllShoes()
    myLogger.info("****All Shoes Found and clicked! ****")


#@then(u'I click the All Shoes link')
#def step_impl(context):



@then(u'close the App')
def step_impl(context):
    context.driver.close()
    myLogger.info("****Browser Closed!****")
