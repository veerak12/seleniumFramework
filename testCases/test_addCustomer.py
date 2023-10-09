import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from random_email import generate_random_email
import time 
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getuserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup: WebDriver):
        self.logger.info('*************** Test_003 AddCustomer****************')
        self.driver =setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login Successful*************")
        time.sleep(3)

        self.logger.info("******Starting Add customer***********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCutomersMenu()
        time.sleep(3)
        self.addCust.clickCutomersMenuItem()
        self.addCust.clickOnAddnew()
        self.logger.info("************ Providing customer Info")

        self.email = generate_random_email()
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("Testcase003")
        self.addCust.setFirstName("Rock")
        self.addCust.setLastName("Star")
        self.addCust.setGender("Male")
        self.addCust.setDOB("10/10/2025")
        self.addCust.setCompanyName("Product Based Company")
        self.addCust.setTax()
        #self.addCust.setNewsLetter("Your store name")
        #self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerVendor("Vendor 2")
        self.addCust.setActiveButton()
        self.addCust.setAdminComment("This is for testing purpose.....")
        self.addCust.clickSave()

        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")

        # Find the <div> element and get its text content
        div_element = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']")
        self.msg = div_element.text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("************ Add customer Test Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("************* Add customer Test Failed ************")
            assert False


        self.driver.close()
        self.logger.info("********* Add customer Test Ended***********") 