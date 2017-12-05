#coding=utf-8

from  selenium import webdriver
import time
import unittest
import HTMLTestRunner

class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.testurl = "xxxxxxx"


    #定义登录方法
    def login(self, username, password):
        driver = self.driver
        driver.get(self.testurl)
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name('btn').click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('xxxx','xxxx')
        name = self.driver.find_element_by_css_selector('.name').text
        self.assertTrue('No_matter' in name)

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('xxxx','xxxx')
        time.sleep(2)
        error_message = self.driver.find_element_by_css_selector('#login_form > ul > li.error').text
        self.assertEqual(u'用户名或密码错误',error_message)

    def test_username_error(self):
         '''用户名错误、密码正确'''
         self.login('xxxx','xxxx')
         time.sleep(2)
         error_message = self.driver.find_element_by_css_selector('#login_form > ul > li.error').text
         self.assertEqual(u'用户名或密码错误',error_message)
         #self.driver.get_screenshot_as_file("C:\Temp\\username_error.jpg")

    def test_username_null(self):
        '''用户名为空，密码正确'''
        self.login('','xxxxx')
        error_message = self.driver.find_element_by_css_selector('#login_form > ul > li.error').text
        #self.assertEqual(u'用户名或密码错误',error_message)


    def tearDown(self):
        time.sleep(2)
        print ('测试完毕')
        self.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()

    suit.addTest(LoginCase('test_login_success'))
    suit.addTest(LoginCase('test_login_pwd_error'))
    suit.addTest(LoginCase('test_username_error'))
    suit.addTest(LoginCase('test_username_null'))

    filename= 'F:\\Github\\Selenium-python\\Report\\nalalogin.html'

    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='nalatestlogin',description='testreport')
    runner.run(suit)
    fp.close()






