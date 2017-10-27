#coding=utf-8
from selenium import webdriver
import time
#读取本地文件
file = open("c:\\Temp\\info.txt","r")
values = file.readlines()
print  values
file.close()
for search in values:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    driver.find_element_by_id("su").submit()
    time.sleep(2)
    driver.quit()

#数据驱动实例
