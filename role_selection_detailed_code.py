import time

class YourPageObject:
    # Assuming you have defined these element locators as class variables
    txtcustomerRoles_xpath = "your_xpath_here"
    lstitemRegistered_xpath = "your_xpath_here"
    lstitemAdministrators_xpath = "your_xpath_here"
    lstitemGuests_xpath = "your_xpath_here"
    lstitemVendors_xpath = "your_xpath_here"

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        # Determine the current selected roles
        is_registered_selected = self.isRoleSelected(self.lstitemRegistered_xpath)
        is_guests_selected = self.isRoleSelected(self.lstitemGuests_xpath)

        if role == 'Registered':
            role_xpath = self.lstitemRegistered_xpath
            # Unselect 'Guests' if it's selected
            if is_guests_selected:
                self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
                #self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.lstitemGuests_xpath))
        elif role == 'Guests':
            role_xpath = self.lstitemGuests_xpath
            # Unselect 'Registered' if it's selected
            if is_registered_selected:
                self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
                #self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.lstitemRegistered_xpath))
        elif role == 'Administrators':
            role_xpath = self.lstitemAdministrators_xpath
        elif role == 'Vendors':
            role_xpath = self.lstitemVendors_xpath
        else:
            role_xpath = self.lstitemGuests_xpath  # Default to 'Guests'

        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(role_xpath))
        time.sleep(3)

    def isRoleSelected(self, role_xpath):
        # Check if a role is selected by checking its class attribute
        element = self.driver.find_element_by_xpath(role_xpath)
        return "k-state-selected" in element.get_attribute("class")
