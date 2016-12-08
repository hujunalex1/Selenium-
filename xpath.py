#coding=utf-8
import  time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
#id 定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys("hello")
driver.find_element_by_xpath("//input[@id='su']").click()

#class 定位
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("hujun")
driver.find_element_by_xpath("//*[@class='btn self-btn bg s_btn']").click()

#使用逻辑运算符
driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']/span/input")


driver.quit()
