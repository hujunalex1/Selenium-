#coding=utf-8

from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import public
import time
driver = webdriver.Chrome()
driver.get("http://www-test.lizi.com")

#调用登录模块
public.login(driver)


#调用退出模块
public.logout(driver)



