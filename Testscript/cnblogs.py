#coding=utf-8
"""

乙醇的一个表单提交实例

"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://jinshuju.net/f/kRXoEv")
driver.implicitly_wait(5)
#给5星
driver.find_element_by_xpath("//div[@class='selectable type-star']/i[5]").click()#使用索引来定位
#勾选selenium
driver.find_element_by_class_name("check-box-wrapper").find_element_by_class_name("selected-icon").click()#层级定位
#输入建议内容
driver.find_element_by_xpath("//*[@id='entry_field_3']").send_keys(u'上面的checkbox无法定位，怎么实现？')
#输入联系方式
driver.find_element_by_css_selector("#entry_field_4").send_keys("huj@lizi.com")
time.sleep(2)
#点击提交按钮
driver.find_element_by_name("commit").click()

driver.quit()


