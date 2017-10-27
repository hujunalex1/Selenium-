# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner
from HTML_Test_Report import Baidu
search = unittest.TestSuite()

search.addTest(Baidu('test_bd_search'))

filename = 'c:\\Temp\\report.html'

fp = file(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"百度搜索测试报告",description="用例执行情况：")

runner.run(search)

fp.close()


