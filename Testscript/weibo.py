#coding=utf-8
from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.weibo.com")
driver.implicitly_wait(2)
driver.find_element_by_id('loginname').send_keys('###')
