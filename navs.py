#coding:utf-8

from selenium import webdriver
import os
import time
driver = webdriver.Chrome()
file = os.path.abspath("nav.html")
driver.get(file)
#driver.maximize_window()
driver.implicitly_wait(5)
#层级关系定位
n = driver.find_element_by_class_name("nav").find_element_by_link_text("About")
n.click()

#link_text 定位
#driver.find_element_by_link_text("About").click()




