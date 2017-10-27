#coding=utf-8

from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://m.lizi.com")

#参数数字为像素点

print "设置浏览器宽480、高800显示"
driver.set_window_size(480,800)
time.sleep(5)
driver.quit()





