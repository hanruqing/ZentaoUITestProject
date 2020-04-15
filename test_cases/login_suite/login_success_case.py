import HTMLTestRunner
import unittest
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

current = os.path.dirname(__file__)
firefox_driver_path = os.path.join(current, '../../webdriver/geckodriver')

class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None: #把selenium初始化配置放入
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')

    def tearDown(self) -> None: #测试清理：浏览器关闭 注册
        time.sleep(2)
        self.driver.quit()

    def test_login1(self):
        '''case01 使用admin Aa123456 测试能否登录'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Aa123456')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        actual_res=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(actual_res,'admin','test_login用例执行失败')

    def test_login2(self):
        '''case02 使用dev01 Aa123456 测试能否登录'''
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('dev01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Aa123456')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//span[@class="user-name"]'),'dev01'),'test_login用例执行失败')
if __name__=='__main__':
    unittest.main()