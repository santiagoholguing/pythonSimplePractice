
from selenium import webdriver
from selenium.webdriver.common.by import By

class Home():

    def __init__(self, driver):
        self.driver = driver

    def access_signin(self):

        self.driver.find_element(by=By.CSS_SELECTOR, value='.login').click()




    # elements = {
    #     getBtnLogin: driver.find_element(by=By.CSS_SELECTOR, value='.login')
    # }
    #
    #
    # def accessBtnLogin(self):
    #     self.elements.get(getBtnLogin).click()







