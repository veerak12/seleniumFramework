import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    lnkCustomers_menu_xpath = "(//a[@class='nav-link'])[21]"
    lnkCustomers_menuitem_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_AddNew_xpath = "(//a[normalize-space()='Add new'])[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdGenderMale_id_xpath = "//input[@id='Gender_Male']"
    rdGenderFemale_id_xpath = "//input[@id='Gender_Female']"
    txtDateofBirth_xpath = "//input[@id='DateOfBirth']"
    txtCompanyname_xpath = "//input[@id='Company']"
    #txtJenish_xpath = "(//input[@id='customer_attribute_1'])[1]"
    checkTaxExempt_ID = "IsTaxExempt"
    lstBox_Newsletter_xpath = "(//div[@role='listbox'])[1]"
    lstitem_Storename_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_taglist"]/li/span[1]'
    lstitem_TestStore2_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_taglist"]/li[2]/span[1]'
    lstBox_Customerroles_xpath = "(//div[@role='listbox'])[2]"
    lstBox_CustomerrolesAdmin_xpath = "//span[normalize-space()='Administrators']"
    lstBox_CustomerrolesRegistered_xpath = "//span[normalize-space()='Registered']"
    lstBox_CustomerrolesGuests_xpath = "(//span[normalize-space()='Guests'])[1]"
    lstBox_CustomerrolesVendors_xpath= "//span[normalize-space()='Vendors']"
    lstBox_deleteBtn_xpath = "//span[@title='delete']" 
    drpd_Vendor_xpath = "//select[@id='VendorId']"
    check_Active_id = "Active"
    txt_Admincomment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
    
    def clickCutomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()
    
    def clickCutomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()
    
    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstname_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastname_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdGenderMale_id_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdGenderFemale_id_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdGenderMale_id_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDateofBirth_xpath).send_keys(dob)
    
    def setCompanyName(self,company_name):
        self.driver.find_element(By.XPATH, self.txtCompanyname_xpath).send_keys(company_name)

    def setTax(self):
        self.driver.find_element(By.ID, self.checkTaxExempt_ID).click()
    
    def setNewsLetter(self,role):
        # self.driver.find_element(By.XPATH, self.lstBox_Newsletter_xpath).click()
        # time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lstBox_Newsletter_xpath)))

        # Click the dropdown
        self.driver.find_element(By.XPATH, self.lstBox_Newsletter_xpath).click()

        if role == "Your store name":
            lst_item =self.driver.find_element(By.XPATH, self.lstitem_Storename_xpath)
        elif role == "Test store 2":
            lst_item =self.driver.find_element(By.XPATH, self.lstitem_TestStore2_xpath)
        else:
            lst_item =self.driver.find_element(By.XPATH, self.lstitem_Storename_xpath)
        time.sleep(3)
        #self.listitem.click() click doesn't works that why used java script code
        self.driver.execute_script("arguments[0].click();", lst_item)


    
    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.lstBox_Customerroles_xpath).click()
        time.sleep(3)

        if role == "Administrators":
            lst_item =self.driver.find_element(By.XPATH, self.lstBox_CustomerrolesAdmin_xpath)
        elif role == "Registered":
            lst_item =self.driver.find_element(By.XPATH, self.lstBox_CustomerrolesRegistered_xpath)
        elif role == "Guests":
            # Here user can be Registered( or) Guest, only one selected removing the existing ones
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.lstBox_deleteBtn_xpath).click()
            lst_item = self.driver.find_element(By.XPATH, self.lstBox_CustomerrolesGuests_xpath)
        elif role == "Vendors":
           lst_item = self.driver.find_element(By.XPATH, self.lstBox_CustomerrolesVendors_xpath)
        else:
            lst_item = self.driver.find_element(By.XPATH, self.lstBox_CustomerrolesGuests_xpath)
        time.sleep(3)

        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", lst_item)


    def setManagerVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpd_Vendor_xpath))
        drp.select_by_visible_text(value)

    def setActiveButton(self):
        self.driver.find_element(By.ID, self.check_Active_id).click()

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH, self.txt_Admincomment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()