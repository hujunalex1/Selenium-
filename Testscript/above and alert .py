#coding=utf-8

from  selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

drive = webdriver.Chrome()
drive.get("http://www.baidu.com")
above = drive.find_element_by_link_text('设置')
ActionChains(drive).move_to_element(above).perform()
time.sleep(2)
drive.find_element_by_link_text(u"搜索设置").click()
time.sleep(2)

s = Select(drive.find_element_by_id('nr'))
s.select_by_visible_text(u'每页显示20条')

time.sleep(2)

drive.find_element_by_link_text(u'保存设置').click()

time.sleep(2)

t= drive.switch_to.alert
print t.text
t.accept() #确认点击
#t.dismiss()#相当于右上角关掉按钮

time.sleep(2)

drive.quit()

