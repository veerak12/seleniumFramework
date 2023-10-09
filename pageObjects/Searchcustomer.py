from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    #table_xpath = "//div[@class='dataTables_scroll']"
    table_xpath= "//table[@id='customers-grid']"
    table_rows_xpath = '//*[@id="customers-grid"]/tbody/tr'
    table_columns_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)
    
    def setFirstName(self,name):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(name)

    def setLastName(self,name):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(name)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        rows = self.driver.find_elements(By.XPATH, self.table_rows_xpath)
        return len(rows)
    
    def getNoOfColumns(self):
        columns = self.driver.find_element(By.XPATH, self.table_columns_xpath)
        return len(columns)
    
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, f'//*[@id="customers-grid"]/tbody/tr[{r}]/td[2]').text
            if emailid == email:
                flag = True
                break
        return flag

    
    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            first_name = table.find_element(By.XPATH, f'//*[@id="customers-grid"]/tbody/tr[{r}]/td[3]').text
            if name == first_name:
                flag = True
                break
        return flag
         

# code not using for loop only for the first row in the table
#this code is also used for email also
    # def searchCustomerByName(self, name):
    #     flag = False
    #     table =  self.driver.find_element(By.XPATH, self.table_xpath)
    #     first_name = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr[1]/td[3]').text
    #     if name == first_name:
    #         flag =True
    #     return flag

        




