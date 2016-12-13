#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#鼠标悬停在设置上
link = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(link).perform()

#点击搜索设置按钮
driver.find_element_by_class_name("setpref").click()

#点击保存按钮
driver.find_element_by_css_selector("#gxszButton > a.prefpanelgo").click()

#接收弹窗
driver.switch_to.alert().accept()

time.sleep(3)
driver.quit()
