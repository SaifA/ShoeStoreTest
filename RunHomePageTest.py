import time

from selenium import webdriver

class ShoeStorePageTest():
    driver = None

    def testBrowser(self):
        baseUrl = "https://shoe-store-july.herokuapp.com/"
        ShoeStorePageTest.driver = webdriver.Chrome()
        ShoeStorePageTest.driver.get(baseUrl)
        time.sleep(5)

    def VerifyHomePage(self):
        elementByXpath = ShoeStorePageTest.driver.find_element_by_xpath("//h2[normalize-space()='Welcome to Shoe Store!']").is_displayed()
        if elementByXpath is True:
            print("Welcome to Shoe Store Homepage!")
        else:
            print("Homepage not found!")
            time.sleep(5)



    def navBartest(self):
        elementByXpath = ShoeStorePageTest.driver.find_element_by_xpath("//a[normalize-space()='All Shoes']").click()
        time.sleep(5)
        if elementByXpath is True:
            print("Shoe Store link clicked!")
        else:
            print("All Shoes link didn't navigate to the Page!")

    def emailUserInputTest(self):
        elementByID = ShoeStorePageTest.driver.find_element_by_id("remind_email_input").send_keys("xyz@example.com")
        time.sleep(5)
        if elementByID is True:
            print("Email Input field found, click and typed an valid email ID")
        else:
            print("Email Input field not found!")



    def emailSubmitQueryTest(self):
        elementByID = ShoeStorePageTest.driver.find_element_by_id("remind_email_submit").click()
        time.sleep(5)
        if elementByID is True:
            print("Email Input field found, click and typed an valid email ID")
        else:
            print("Email Input field not found!")

        time.sleep(5)


    def promotionalCodeInputTest(self):
        ShoeStorePageTest.driver.find_element_by_id("promo_code_input").send_keys("xyz123")
        time.sleep(5)
        print("Promo code Input field found and clicked!")



    def promotionalCodeSubmitTest(self):
         ShoeStorePageTest.driver.find_element_by_id("promo_code_submit").click()
         time.sleep(5)
         print("Promo code's Submit Query button found and clicked!")
         ShoeStorePageTest.driver.quit()

ssTest = ShoeStorePageTest()
ssTest.testBrowser()
ssTest.VerifyHomePage()
ssTest.navBartest()
ssTest.emailUserInputTest()
ssTest.emailSubmitQueryTest()
ssTest.promotionalCodeInputTest()
ssTest.promotionalCodeSubmitTest()


