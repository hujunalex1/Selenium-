#coding=utf-8

from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#class 定位

driver.find_element_by_css_selector(".s_ipt").send_keys("python")
driver.find_element_by_css_selector(".bg s_btn").click()

#ID 定位
driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()

#通过父子关系定位
driver.find_element_by_css_selector("span>input").send_keys("test")


#通过属性定位
driver.find_element_by_css_selector("input[autocomplete='off']").send_keys("off")
driver.find_element_by_css_selector("input[type='submit']").click()



time.sleep(3)
driver.quit()
