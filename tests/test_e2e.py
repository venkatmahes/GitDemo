from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.BaseClass import BaseClass
from pageobjects.HomePage import HomePage
from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.ConfirmPage import ConfirmPage
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopitems()
        log.info("getting all the product names")
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        checkoutpage.getcheckout1().click()
        confirmpage = checkoutpage.getcheckout2()
        log.info("enter country as ind")
        confirmpage.getcountry().send_keys("ind")
        self.verifylinkpresence("India")
        confirmpage.getcountry2().click()
        confirmpage.getcheckbox().click()
        confirmpage.getsubmitt().click()
        print(self.driver.find_element_by_class_name("alert-success").text)
