import time
import unittest
from cgitb import text

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
time.sleep(1)
#driver.find_element_by_css_selector('.login').click()
driver.find_element(by=By.CSS_SELECTOR, value='.login').click()
#driver.find_element_by_css_selector('#email_create').send_keys("santiholguing@gmail.com")
driver.find_element(by=By.CSS_SELECTOR, value='#email_create').send_keys('stttss@gszsssbs.com')
driver.find_element(by=By.CSS_SELECTOR, value='.icon-user').click()
#driver.find_element_by_css_selector('').click()
#driver.find_element_by_css_selector('#customer_firstname').send_keys("Santiago")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'customer_firstname')))
driver.find_element(by=By.CSS_SELECTOR, value='#customer_firstname').send_keys('santiago')
driver.find_element(by=By.CSS_SELECTOR, value='#customer_lastname').send_keys('Holguin Giraldo')
driver.find_element(by=By.CSS_SELECTOR, value='#passwd').send_keys('Santi123f456')
driver.find_element(by=By.CSS_SELECTOR, value='#days>option[value=\'10\']').click()
Select(driver.find_element(by=By.CSS_SELECTOR, value='#months')).select_by_visible_text('November ')
Select(driver.find_element(by=By.CSS_SELECTOR, value='#years')).select_by_value('1995')
driver.find_element(by=By.CSS_SELECTOR, value='#newsletter').click()
driver.find_element(by=By.CSS_SELECTOR, value='#firstname').send_keys('first name example')
driver.find_element(by=By.CSS_SELECTOR, value='#address1').send_keys('adress Last name example')
driver.find_element(by=By.CSS_SELECTOR, value='#company').send_keys('company example')
driver.find_element(by=By.CSS_SELECTOR, value='#city').send_keys('city example')
Select(driver.find_element(by=By.CSS_SELECTOR, value='#id_state')).select_by_value('11')
driver.find_element(by=By.CSS_SELECTOR, value='#postcode').send_keys('12345')
driver.find_element(by=By.CSS_SELECTOR, value='#phone_mobile').send_keys('3001221221')
driver.find_element(by=By.CSS_SELECTOR, value='#alias').send_keys('alias example')
driver.find_element(by=By.CSS_SELECTOR, value='#submitAccount').click()
print()
#assert(driver.find_element(by=By.CSS_SELECTOR, value='.account>span')=="santiago Holguin Giraldo"),"Esta malo, ese no es el nombre correcto"


class mis_test(unittest.TestCase):

    def test_mensaje(self):

        self.assertEqual(driver.find_element(by=By.CSS_SELECTOR, value='.account>span').text, 'santiago Holguin Giraldo', "Comparison Done")

if __name__ == '__main__':
    unittest.main()