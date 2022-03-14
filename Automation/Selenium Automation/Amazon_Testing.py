from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys
import sys

class test_project(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Selenium Browser Drivers\chromedriver.exe")
        cls.driver.get("https://www.amazon.in/")

    def test1_is_displayed(self):
        button1 = self.driver.find_element_by_class_name("nav-search-field")
        sleep(2)
        print("After is_displayed ", button1.is_displayed())
        self.assertTrue(button1.is_displayed())

    def test2_is_enabled(self):
        button2 = self.driver.find_element_by_id("twotabsearchtextbox")
        #button3.click()
        sleep(2)
        print("After is_enabled ", button2.is_enabled())
        self.assertTrue(button2.is_enabled())

    def test3_is_clicked(self):
        button3 = self.driver.find_element_by_class_name("nav-search-field ")
        print("Before is_clicked ")
        sleep(2)
        button3.click()
        print("After is_clicked ")
        sleep(4)


    def test4_is_back(self):
        back_button = self.driver.find_element_by_id('twotabsearchtextbox')
        back_button.click()
        sleep(3)
        cur_url = self.driver.current_url
        self.assertEqual(cur_url, 'https://www.amazon.in/')

    def test5_scroll(self):
        elem = self.driver.find_element_by_tag_name('html')
        elem.send_keys(Keys.END)
        sleep(4)
        elem.send_keys(Keys.END)
        sleep(5)
        elem.send_keys(Keys.HOME)
        sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_project('test1_is_displayed'))
    suite.addTest(test_project('test2_is_enabled'))
    suite.addTest(test_project('test3_is_clicked'))
    suite.addTest(test_project('test4_is_back'))
    suite.addTest(test_project('test5_scroll'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

