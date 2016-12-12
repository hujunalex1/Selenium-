#coding=utf-8

from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element=driver.find_element_by_xpath("//*[@id='lg']/img")
target = driver.find_element_by_id("kw")
ActionChains(driver).drag_and_drop(element,target).perform()

driver.quit()
