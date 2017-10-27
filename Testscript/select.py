#coding=utf-8
from selenium import  webdriver
import time
import  os
from  selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
file = os.path.abspath('c:\\Temp\\select.html')
driver.get(file)
assert "test" in driver.title
driver.maximize_window()
select = Select(driver.find_element_by_id("user_select"))#实例化
 #根据文本的值来选择
#select.select_by_visible_text("BYD")
#根据索引来选择，index是用0开始算
#select.select_by_index(2)
#根据option value 来选择
select.select_by_value("audi")
time.sleep(3)
driver.close()
