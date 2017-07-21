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
time.sleep(2)
#切换页面句柄
for handle in driver.window_handles:
    driver.switch_to.window(handle)
time.sleep(2)
#点击保存设置按钮
driver.find_element_by_id("gxszButton").find_element_by_class_name("prefpanelgo").click()

time.sleep(3)
driver.quit()
