import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.Searchcustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_005_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getuserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("********** Search Customer By FirstName Test_005 **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Successful ****************")
        self.logger.info("**************** Starting search customer by username ***********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCutomersMenu()
        time.sleep(3)
        self.addCust.clickCutomersMenuItem()
        self.logger.info("*********** Enter customer first name **********")

        self.SearchCust = SearchCustomer(self.driver)
        self.SearchCust.setFirstName("John")
        self.SearchCust.clickSearch()
        time.sleep(5)
        self.logger.info("********** Searching the Customer By FirstName **********")
        
        status =self.SearchCust.searchCustomerByName("John Smith")
        if status:
            self.logger.info("Customer found. Test Passed.")
            assert True
        else:
            self.logger.info("Customer Not found. Test Failed.")
            assert False
        
        self.driver.close()

        self.logger.info("*********** Test for search customer by First Ended ***************")

    