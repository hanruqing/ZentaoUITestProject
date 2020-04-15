import HTMLTestRunner
import unittest
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import Set_driver
from common import login


class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None: #把selenium初始化配置放入
        self.driver=Set_driver.set_driver()

    def tearDown(self) -> None: #测试清理：浏览器关闭 注册
        time.sleep(2)
        self.driver.quit()


    def test_login(self):
        '''case03 使用dev01 Aa123456 测试能否登录'''
        login.login(self.driver,'admin','Aa123456')
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))


if __name__=='__main__':
    unittest.main()