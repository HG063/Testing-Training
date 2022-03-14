from selenium import webdriver
import unittest
import re


class PhoneTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Selenium Browser Drivers\chromedriver.exe")
        self.driver.get("http://www.airindia.in/customer-support.htm")

    def test(self):
        doc = self.driver.page_source
        numbers = re.findall(r'[\d]{8}',doc)
        print(numbers)
        for number in numbers:
            print(number)
        print("total mobile no are ", len(numbers))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
