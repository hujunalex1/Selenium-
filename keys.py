#coding=utf-8

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#输入框中输入数据
#river.find_element_by_id("kw").send_keys("seleniumm")
#time.sleep(4)
#删除多输入的m
#driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#输入空格键+ “教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")

#ctrl + a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)

#ctrl + x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)

#ctrl + v
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#通过回车键盘来代替点击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()

