from selenium import webdriver
import unittest
import re


class EmailTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Selenium Browser Drivers\chromedriver.exe")
        self.driver.get("http://www.airindia.in/customer-support.htm")

    def test(self):
        doc = self.driver.page_source
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
        for email in emails:
            print(email)
        print(f"Total email address present is {len(email)}")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
