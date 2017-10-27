#coding=utf-8

from selenium import webdriver
#引入ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
right_click = driver.find_element_by_id("su")
ActionChains(driver).context_click(right_click).perform()


'''
ActionChains 类提供的鼠标操作的常用方法：
 perform() 执行所有ActionChains 中存储的行为
 context_click() 右击
 double_click() 双击
 drag_and_drop() 拖动
 move_to_element() 鼠标悬停

'''
