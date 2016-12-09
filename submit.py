#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://youdao.com/")
driver.find_element_by_id("translateContent").send_keys("selenium")

#submit()方法用于提交表单，这里特别用于没提交按钮的情况，例如搜索框输入关键字之后的“回车”
driver.find_element_by_css_selector("input[name='q']").submit()
driver.find_element_by_xpath("/html/body/div[7]/i/a[1]").click()

time.sleep(5)
driver.quit()



