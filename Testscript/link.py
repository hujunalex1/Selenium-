#coding=utf-8
from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_link_text("新闻").click() # link 定位
driver.quit()
