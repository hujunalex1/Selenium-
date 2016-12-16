#coding=utf-8
import time
#login

def login(driver):
    driver.find_element_by_class_name("ui-dialog-close").click() #关闭弹窗
    driver.find_element_by_xpath("//*[@id='topbar_nav']/li[1]/a[1]").click()#点击登录按钮
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("18055352262")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("hj123456")
    driver.find_element_by_xpath("//input[@class='btn']").click()#点击确认登录按钮

#logout


def logout(driver):
    time.sleep(2)
    driver.find_element_by_link_text(u"退出").click()
    driver.quit()
