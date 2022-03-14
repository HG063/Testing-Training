from selenium import webdriver
from time import sleep
browser=webdriver.Chrome(executable_path="C:\Selenium Browser Drivers\chromedriver.exe")
print (dir(browser))
browser.get('https://www.python.org')
sleep(15)
browser.close()