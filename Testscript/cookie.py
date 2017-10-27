#coding=utf-8

from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#获取cookie信息
cookie = driver.get_cookies()
print cookie

#向cookie 的name 和value 添加会话信息
driver.add_cookie({"name":"key-aaaaaa","value":"value-bbbbb"})

#遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie["name"],cookie["value"])


#返回有特定name 值有cookie 信息
c = driver.get_cookie("key-aaaaaa")
print c

#删除指定name的cookie
s = driver.delete_cookie("key-aaaaaa")
print s
