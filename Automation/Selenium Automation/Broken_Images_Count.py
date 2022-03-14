import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

class imageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Selenium Browser Drivers\chromedriver.exe")
    def test_broken(self):
        self.URL = "https://the-internet.herokuapp.com/broken_images"
        self.BrokenImageCount = 0
        self.driver.get(self.URL)
        image_list = self.driver.find_elements(By.TAG_NAME, "img")
        print('Total number of images on ' + self.URL + ' are ' + str(len(image_list)))

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    self.BrokenImageCount = (self.BrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")

    def tearDown(self):
        self.driver.close()
        print('The page ' + self.URL + ' has ' + str(self.BrokenImageCount) + ' broken images')

if __name__ == '__main__':
    unittest.main()