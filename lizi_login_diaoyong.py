# coding=utf-8

from  selenium import webdriver
import public

driver = webdriver.Chrome()
driver.get("http://www-test.lizi.com")

# 调用登录模块
public.login(driver)

# 调用退出模块
public.logout(driver)
