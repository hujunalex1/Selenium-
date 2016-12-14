#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
driver = webdriver.Chrome()
#打开网盘
driver.get("https://pan.baidu.com")
#显示等待，为了定位元素，因为弹出框较慢显示出来。
driver.implicitly_wait(10)
#输入用户名
driver.find_element_by_css_selector("input[name='userName']").send_keys("18267200735")
#输入密码
driver.find_element_by_css_selector("input[name='password']").send_keys("hj673320")
#sumbit
driver.find_element_by_css_selector("input[name='password']").submit()
#关闭弹出框
driver.find_element_by_css_selector("body > div.welcome-box > div.welcome-close.icon.icon-close.close-addAnimation").click()
#等待3秒去点击上传按钮
time.sleep(3)
#上传文件
driver.find_element_by_id("h5Input0").send_keys("c:\\Temp\\frame.html")
time.sleep(3)
driver.quit()

