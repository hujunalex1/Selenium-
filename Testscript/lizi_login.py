#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www-test.lizi.com/")
driver.implicitly_wait(5)

def login():
    driver.find_element_by_class_name("ui-dialog-close").click()
    driver.find_element_by_xpath("//*[@id='topbar_nav']/li[1]/a[1]").click()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("18055352262")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("hj123456")
    driver.find_element_by_xpath("//input[@class='btn']").click()

def logout():
    driver.find_element_by_link_text(u"退出").click()
    time.sleep(2)
    driver.quit()

login()

logout()


