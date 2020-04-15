import HTMLTestRunner
import unittest
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current = os.path.dirname(__file__)
firefox_driver_path = os.path.join(current, '../../webdriver/geckodriver')

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None: #把selenium初始化配置放入
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')

    def tearDown(self) -> None: #测试清理：浏览器关闭 注册
        time.sleep(2)
        self.driver.quit()


    def test_my_link(self):
        '''case04 验证我的地盘菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('dev01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Aa123456')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

    def test_product_link(self):
        '''case05 验证产品菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('dev01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Aa123456')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is("产品主页 - 禅道"))


if __name__=='__main__':
    unittest.main()