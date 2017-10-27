#coding:utf-8

'''
获取测试对象的css属性场景

当你的测试用例纠结细枝末节的时候，你就需要通过判断元素的css属性来验证你的操作是否达到了预期的效果。
比如你可以通过判断页面上的标题字号以字体来验证页面的显示是否符合预期。
当然，这个是强烈不推荐的。因为页面上最不稳定的就是css了，css变动频繁，
而且通过属性也不能直观的判断页面的显示效果，还不如让人为的去看一眼，
大问题一望即知。

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
link = driver.find_element_by_id("su")
print link.value_of_css_property("background")
print driver.find_element_by_link_text("新闻").value_of_css_property("font-size")
time.sleep(2)
driver.quit()
