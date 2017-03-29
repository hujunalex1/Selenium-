#coding=utf-8

from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("su").click()
time.sleep(4)
driver.quit()

