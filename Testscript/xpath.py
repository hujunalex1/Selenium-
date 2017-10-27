#coding=utf-8
import  time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
#id 定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys("hello")
driver.find_element_by_xpath("//input[@id='su']").click()

#class 定位
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("hujun")
driver.find_element_by_xpath("//*[@class='btn self-btn bg s_btn']").click()

#使用逻辑运算符
driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']/span/input")


driver.quit()

#补充一部分xpath定位方法
HTML列子

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

##form元素可以这样定位

login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")

   1. 绝对路径（如果HTML有细微的改变就会失效）
   2. HTML的第一个form元素
   3. id属性为’loginForm’的form元素

##username元素可以这样定位

username = driver.find_element_by_xpath("//from[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")


   1. 第一个form元素的 name属性是’username’的input子元素
   2. id属性为’loginForm’的form元素的第一个input子元素
    3.name属性为’username’的第一个input元素
