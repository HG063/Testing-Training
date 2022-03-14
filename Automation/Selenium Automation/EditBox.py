import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class simpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Selenium Browser Drivers\chromedriver.exe")

    def test_clear(self):
        self.driver.get("https://ashokonmi3.github.io/Selenium.Pages/login.html")
        elem = self.driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("root")
        self.driver.find_element_by_name("password").send_keys("root")
        self.driver.find_element_by_xpath("/html/body/form/input[3]").send_keys(Keys.ENTER)
        sleep(5)

    def test_isEnabled(self):
        self.driver.get("https://ashokonmi3.github.io/Selenium.Pages/disabledEditBox.html")
        elem = self.driver.find_element_by_name("lname")
        sleep(5)
        self.assertFalse(elem.is_enabled())
        sleep(2)

    def test_isdisplayed(self):
        self.driver.get("https://ashokonmi3.github.io/Selenium.Pages/disabledEditBox.html")
        elem = self.driver.find_element_by_name("lname")
        sleep(5)
        self.assertTrue(elem.is_displayed())
        sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()