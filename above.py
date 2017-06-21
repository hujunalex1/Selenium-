#coding=utf-8

from  selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
drive = webdriver.Chrome()
drive.get("http://www.baidu.com")
above = drive.find_element_by_link_text('设置')
ActionChains(drive).move_to_element(above).perform()
time.sleep(2)
drive.find_element_by_link_text(u"高级搜索").click()
time.sleep(2)
drive.quit()

