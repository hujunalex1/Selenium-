#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://www.lizi.com")
#打开登录界面
driver.find_element_by_class_name("ui-dialog-close").click() #关闭弹出广告
time.sleep(2)
driver.find_element_by_xpath("//*[@id='topbar_nav']/li[1]/a[1]").click()

print  'before login ========='

#打印当前页面title
title = driver.title
print title

#打印当前页面URL
now_url = driver.current_url
print now_url

#执行登录
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("18267200735")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("password")
driver.find_element_by_id("password").send_keys(Keys.ENTER)

print 'After login================'

#再次打印title
title = driver.title
print title

#再次打印URL

now_url = driver.current_url
print now_url

#获取登录名
username= driver.find_element_by_css_selector(".name").text
print username


