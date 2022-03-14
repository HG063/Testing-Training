import unittest
from selenium import webdriver
from time import sleep

class simpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Selenium Browser Drivers\chromedriver.exe")
        self.driver.get("https://ashokonmi3.github.io/Selenium.Pages/SEL_01_WebDriverDemoWebsite.html")

    def test_select(self):
        radio_button = self.driver.find_element_by_id("magazines-radio-btn")
        radio_button.click()
        sleep(5)
    def test_isselect(self):
        checkbox = self.driver.find_element_by_id("bicycle-checkbox")
        sleep(2)
        self.assertFalse(checkbox.is_selected())
        checkbox.click()
        self.assertTrue(checkbox.is_selected())
        sleep(2)
    def test_isdisplayed(self):
        checkbox = self.driver.find_element_by_id("bicycle-checkbox")
        self.assertTrue(checkbox.is_displayed())
        sleep(2)
    def test_isenabled(self):
        radio_button = self.driver.find_element_by_id("tricycle-checkbox")
        self.assertFalse(radio_button.is_enabled())
        sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()