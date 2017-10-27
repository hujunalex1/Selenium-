#coding=utf-8

from  selenium import webdriver
import time
import unittest

class ordertest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.baseurl ="http://www-test.lizi.com"
        self.driver.implicitly_wait(10)

    def test_case(self):
        driver = self.driver
        driver.get(self.baseurl)
        time.sleep(2)
       # driver.maximize_window()
        #点击关闭弹出广告按钮
        driver.find_element_by_css_selector(".ui-dialog-close").click()
        #点击登录按钮
        driver.find_element_by_xpath("//*[@id='topbar_nav']/li[1]/a[1]").click()
        #清除用户名输入框原数据
        driver.find_element_by_id("username").clear()
        #输入用户名
        driver.find_element_by_id("username").send_keys("18267200735")
        #清除密码输入框原数据
        driver.find_element_by_id("password").clear()
        #输入密码
        driver.find_element_by_id("password").send_keys("hj123456")
        #点击登录按钮
        driver.find_element_by_xpath("//input[@type='submit' and @class='btn']").click()
        #返回首页在查询输入框输入数据
        driver.find_element_by_id("textfield").send_keys(u"面膜")
        #点击搜索按钮
        driver.find_element_by_class_name("sea_submit").click()
        time.sleep(2)
        #选择第一个商品，进入详细页
        driver.find_element_by_css_selector("#productlist > ul > li:nth-child(1) > a > img").click()
        time.sleep(2)
        #切换句柄
        driver.switch_to.window(driver.window_handles[1])
        #选择一个规格
        driver.find_element_by_partial_link_text(u"绿茶").click()
        #点击加入购物车按钮
        driver.find_element_by_id("buy_btn").click()
        time.sleep(2)
        #点击去购物车结算按钮
        driver.find_element_by_partial_link_text(u"结算").click()
        #点击全选按钮
        driver.find_element_by_css_selector("#page > div.cart_list > div.cart_th > ul > li.td.td_chk > span").click()
        #点击结算按钮
        driver.find_element_by_id("topay").click()
        #点击提交订单按钮
        driver.find_element_by_link_text(u"提交订单").click()
        #点击确认付款按钮
        driver.find_element_by_css_selector("input[type='submit']").click()
        #去我的订单页面
        driver.switch_to.window(driver.window_handles[2])#识别不到 进行句柄切换
        driver.find_element_by_link_text(u"我的订单").click()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



    if __name__ == '__main__':
        unittest
