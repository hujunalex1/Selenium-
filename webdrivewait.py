#coding=utf-8

from  selenium import webdriver
from  selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待方法
driver.get("http://www.baidu.com")

#element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))#显示等待方法
#element.send_keys("selenium")

driver.find_element_by_id("kw").send_keys("selenium")
driver.quit()
