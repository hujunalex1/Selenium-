#coding=utf-8
#switch_to_frame() 方法使用

import  os
import  time
from  selenium import webdriver
driver = webdriver.Chrome()
file = os.path.abspath("c:\\Temp\\frame.html")
print file
driver.get(file)

#切换到iframe（id = "if"）  switch_to_frame() 默认可以直接取表单的id 或name 属性进行切换。
driver.switch_to.frame("if")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(4)
driver.quit()

'''
那么如果iframe 没有可用的id 和name 可以通过下面的方式进行定位：
先通过xpath 定位到iframe
xf = driver.find_element_by_xpath('//*[@class="if"]')

再将定位对象传给switch_to_frame()方法

driver.switch_to_frame(xf)

如果完成了在当前表单上的操作可以通过switch_to_default_content()方法返回到上一层表单
driver.switch_to_default_content()

'''
