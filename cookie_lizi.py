#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://www.lizi.com")
#关闭弹出广告
driver.find_element_by_xpath("/html/body/div[15]/div/table/tbody/tr[1]/td/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='topbar_nav']/li[1]/a[1]").click()
#执行登录
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("18267200735")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("nopainnogain5233")
driver.find_element_by_id("password").send_keys(Keys.ENTER)
cookie = driver.get_cookies()
print cookie
for cookie in driver.get_cookies():
    print "%s --> %s" % (cookie["name"],cookie["value"])

