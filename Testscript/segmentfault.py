#coding=utf-8
from  selenium import webdriver
from JunLib import hujunlib
import unittest


class seg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.lib = hujunlib(self.driver)

    def test_login(self):
        self.lib.login_in('222','223')

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
        unittest



