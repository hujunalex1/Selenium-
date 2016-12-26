# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class Unittest01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www-test.lizi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_unittest01(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(2)
        driver.find_element_by_link_text(u"登 录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("18055352262")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("hj123456")
        driver.find_element_by_css_selector("input.btn").click()
        username= driver.find_element_by_css_selector("a.name").text
        self.assertEqual(u"被风吹过的夏天",username )
        print username
        driver.find_element_by_link_text(u"退出").click()

    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
