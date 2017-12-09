#coding=utf-8

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.implicitly_wait(5)

h = driver.current_window_handle  #获取当前窗口句柄

print  h

driver.find_element_by_name('tj_trnews').send_keys(Keys.CONTROL + 't')

all_h = driver.window_handles  #获取所有句柄

print all_h

driver.switch_to.window(all_h[1]) #切换到当前窗口句柄

print  driver.title

driver.close()

driver.switch_to.window(h) #切换到百度首页窗口句柄

print  driver.title










