import os
from selenium import webdriver

def set_driver():
    current = os.path.dirname(__file__)
    firefox_driver_path = os.path.join(current, '../webdriver/geckodriver')
    driver = webdriver.Firefox(executable_path=firefox_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
    return driver