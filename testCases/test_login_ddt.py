import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    # read the properties from the utilities file dynamically no hardcodede needed
    baseURL =  ReadConfig.getApplicationURL()
    path =".//TestData/LoginData.xlsx"  #file location
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup: WebDriver):
        self.logger.info("************** class Test_002_DDT_Login:Test **************")
        self.logger.info("************** Verfying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        #self.driver.maximize_window()
        self.lp = LoginPage(self.driver)  # taking this from the pageObjects LoginPage.py class
        
        self.rows= XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of Rows:", self.rows)
        lst_rows=[]                     #appending the exp pass/fail into the list

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r,1)   #starts with second row and 1st column
            self.password = XLUtils.readData(self.path, "Sheet1",r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3) #test case row pass/fail

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp  == "Pass":
                    self.logger.info('****Passed****')
                    self.lp.clickLogout()
                    lst_rows.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info('****Failed****')
                    self.lp.clickLogout()
                    lst_rows.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.error('****Failed****')
                    self.lp.clickLogout()
                    lst_rows.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info('****Passed****')
                    # self.lp.clickLogout()
                    lst_rows.append("Pass")
        print(lst_rows)
        
        if "Fail" not in lst_rows:
            self.logger.info('******* DDT login test passed *******')
            self.driver.close()
            assert True
        else:
            self.logger.info('******* DDT login test Failed *******')
            self.driver.close()
            assert False
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 *************")
