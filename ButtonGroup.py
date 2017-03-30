#coding:utf-8

from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
file = os.path.abspath("f:\\GitHub\\Selenium-\\button.html")
driver.get(file)
driver.implicitly_wait(5)
buttons = driver.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in buttons:
    if btn.text == 'second':
        print 'find second button'

sleep(2)
driver.quit()
