# coding=utf-8

from  selenium import webdriver

from public import login

driver = webdriver.Chrome()
driver.get("http://www-test.lizi.com")

driver.implicitly_wait(3)
# 调用登录模块
login.login(driver)
# 调用退出模块
login.logout(driver)

driver.quit()

