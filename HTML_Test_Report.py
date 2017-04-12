# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
import HTMLTestRunner #引入HTMLTestRunner 包


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"


    #百度搜索用例

    def test_bd_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":

#测试套件
    suit = unittest.TestSuite()

#添加测试用例到测试套件中
    suit.addTest(Baidu('test_bd_search'))

#定义个报告存放路径
    filename = 'C:\\Temp\\result.html'
    fp = file(filename,'wb')

#定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'百度搜索测试报告',
                                           description = u'用例执行情况:')

#运行测试用例
    runner.run(suit)

#关闭报告文件
    fp.close()





