#coding:utf-8
from time import sleep
from selenium import webdriver
driver =webdriver.Chrome()
driver.get("https://www.zuzuche.com")
driver.find_element_by_link_text(u"门票玩乐").click()
sleep(3)
#获取当前的title
title=driver.title
print(title)
#对title做判断
if title==u"景点门票_特卖门票_门票优惠_打折门票_一日游_特价一日游_玩乐推荐_通票-租租车":
    print("title ok")
else:
    print("title no")
#获取当前的url
now_url=driver.current_url
print(now_url)
#对url做判断
if now_url=="http://poi.zuzuche.com/index-entrance-284ab515c664b25eb22fd29aaf3d553d.html?source=10000":
    print("url ok")
else:
    print("url on")
sleep(3)

driver.quit()
