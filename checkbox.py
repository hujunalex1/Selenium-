#coding=utf-8
import os
import time
from  selenium import webdriver
driver = webdriver.Chrome()
file = os.path.abspath("c:\\Temp\\checkbox.html") #获取文件路径
print file
driver.get(file)

# 选择页面上所有的input 的元素！
inputs = driver.find_elements_by_css_selector("input[type='checkbox']")

#然后从中过滤出tpye 为checkbox 的元素，单击勾选
for i in inputs:
    if i.get_attribute("type") == "checkbox":
        i.click()

print len("checkbox")

time.sleep(4)
driver.quit()



