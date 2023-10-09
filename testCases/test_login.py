import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time  # Import the time module

class Test_001_Login:
    baseURL =  ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getuserPassword()
    logger = LogGen.loggen()

    def get_timestamp(self):
        return time.strftime("%Y%m%d%H%M%S")  # Generate a timestamp as a string

    @pytest.mark.regression
    def test_homePageTitle(self, setup: WebDriver):
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("************** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("************** Home Page Title Test Passed **************")
            self.driver.close()
        else:
            # Generate a unique filename with a timestamp
            screenshot_name = f".\\Screenshots\\test_homePageTitle_{self.get_timestamp()}.png"
            self.driver.save_screenshot(screenshot_name)
            self.logger.info("************** Home Page Title Test Failed **************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup: WebDriver):
        self.logger.info("************** Verfying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login Test Passed **************")
            self.driver.close()
        else:
            # Generate a unique filename with a timestamp
            screenshot_name = f".\\Screenshots\\test_login_{self.get_timestamp()}.png"
            self.driver.save_screenshot(screenshot_name)
            self.logger.info("************** Login Test Failed **************")
            self.driver.close()
            assert False

