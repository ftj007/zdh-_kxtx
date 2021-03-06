from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import unittest

class Testbaidu(unittest.TestCase):
    """docstring for Testbaidu"""

    URL = 'https://www.baidu.com'
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')

    locator_kw = (By.ID,'kw')
    locator_su = (By.ID,'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = self.driver_path)
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)

    def test_baidu_0(self):
        driver = self.driver
        driver.find_element(*self.locator_kw).send_keys('selenium')
        driver.find_element(*self.locator_su).click()
        sleep(2)
        links = driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_baidu_1(self):
        driver = self.driver
        driver.find_element(*self.locator_kw).send_keys('unittest')
        driver.find_element(*self.locator_su).click()
        sleep(2)
        links = driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
