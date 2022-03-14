import unittest
from selenium import webdriver

class Display_Current_URL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Selenium Browser Drivers\chromedriver.exe")

    def test(self):
        self.driver.maximize_window()
        self.driver.get("https://www.zkoss.org/zkdemo/input/radio_button")
        self.driver.get("https://google.com")
        self.driver = self.driver.current_url
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
