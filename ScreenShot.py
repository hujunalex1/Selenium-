#coding=utf-8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


try:
    driver.find_element_by_id("kw_error").send_keys("selenium")
    driver.find_element_by_id("su").click()
except:
    driver.get_screenshot_as_file("d:\\baidu_error.jpg")  #保存截图至指定位置
    driver.quit()
