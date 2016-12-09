#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://login.lizi.com/login?service=http://www.lizi.com/")


driver.find_element_by_css_selector(".text").clear()
driver.find_element_by_css_selector("#username").send_keys("18267200735")
driver.find_element_by_css_selector("input[name='password']").send_keys("password")
driver.find_element_by_class_name("btn").click()
time.sleep(2)
driver.quit()
