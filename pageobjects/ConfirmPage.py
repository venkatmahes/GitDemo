from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    Country = (By.ID, "country")
    Country2 = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitt = (By.CSS_SELECTOR, "[type='submit']")

    def getcountry(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def getcountry2(self):
        return self.driver.find_element(*ConfirmPage.Country2)

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getsubmitt(self):
        return self.driver.find_element(*ConfirmPage.submitt)
