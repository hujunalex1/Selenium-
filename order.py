#coding=utf-8
'''
简单的下单支付流程--自动化
'''
from  selenium import webdriver
import time
import unittest

class ordertest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www-test.meizhuangdaka.com/"
        self.driver.implicitly_wait(5)

    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_link_text(u"请登录").click()
        driver.find_element_by_xpath("//input[@name='userName']").clear()
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("18267200735")
        driver.find_element_by_xpath("//input[@name='password']").clear()
        driver.find_element_by_xpath("//input[@name='password']").send_keys("hj123456")
        driver.find_element_by_xpath("//input[@name='password']").submit()
        #输入snp
        driver.find_element_by_xpath("//input[@name='content']").send_keys("snp")
        #点击搜索按钮
        driver.find_element_by_css_selector("#websearch > button").click()
        #选择第一个商品进行点击，到详细页
        driver.find_element_by_css_selector("#itemlist > ul > li:nth-child(1) > div.pic > a > img").click()
        #切换窗口至新开的页面
        driver.switch_to.window(driver.window_handles[1])
        #加入商品数量
        driver.find_element_by_xpath("//span[@class='num_op add']").click()
        time.sleep(2)
        #点击加入购物车按钮
        driver.find_element_by_id("buybtn").click()
        time.sleep(1)
        #点击弹出的页面上的去购物车结算按钮
        driver.find_element_by_xpath("//*[@id='content:addcart_ok']/div/div[2]/a[2]").click()
        #进入购物车后点击全选按钮
        driver.find_element_by_xpath("//*[@id='page']/div[1]/div[1]/ul/li[1]/span").click()
        #点击去结算按钮
        driver.find_element_by_id("topay").click()
        #进行订单备注
        driver.find_element_by_name("e0d078b5-61f6-4c19-8627-185b59a0d2a0").send_keys("just for unittest")
        #点击提交订单按钮
        driver.find_element_by_id("topay").click()
        #选择付款方式并付款
        driver.find_element_by_css_selector(".btn").click()
        time.sleep(2)
    def tearDown(self):
        driver = self.driver
        time.sleep(2)
        driver.quit()


    if __name__ == '__main__':
        unittest
