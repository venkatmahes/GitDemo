from selenium.webdriver.common.by import By
from pageobjects.ConfirmPage import ConfirmPage
class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getcheckout1(self):
        return self.driver.find_element(*CheckoutPage.checkout1)

    def getcheckout2(self):
        self.driver.find_element(*CheckoutPage.checkout2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
