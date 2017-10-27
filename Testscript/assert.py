#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://segmentfault.com/")
assert "SegmentFault" in driver.title
print  driver.title
