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

class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getuserPassword()
    logger = LogGen.loggen()

    
    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Search Customer By Email Test_004 **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")
        self.logger.info("**********   Starting Search Customer By Email **********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickCutomersMenu()
        time.sleep(3)
        self.addCust.clickCutomersMenuItem()
        self.logger.info("**********Customers page opened **********")

        self.SearchCust = SearchCustomer(self.driver)
        self.SearchCust.setEmail("victoria_victoria@nopCommerce.com")
        self.SearchCust.clickSearch()
        time.sleep(5)
        self.logger.info("********** Searching the Customer By Email **********")

        # status = self.SearchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        # if 'victoria_victoria@nopCommerce.com' in status:
        #     assert True

        status = self.SearchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        if status:
        # Customer found, so the test case passes
            self.logger.info("Customer found. Test Passed.")
            assert True
        else:
            # Customer not found, so the test case fails
            self.logger.info("Customer not found. Test Failed.")
            assert False

        self.driver.close()

        self.logger.info("*********** Test for search customer by email Ended ***************")

