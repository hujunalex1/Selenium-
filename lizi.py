#coding=utf-8
from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.lizi.com")
driver.find_element_by_class_name("ui-dialog-close").click()
driver.find_element_by_id("textfield").send_keys("snp")
driver.find_element_by_class_name("sea_submit").click()
time.sleep(5)
driver.quit()


