from selenium.webdriver.common.by import By

def login(driver,username,passwd):
    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('dev01')
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Aa126')
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
