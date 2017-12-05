#coding=utf-8

from selenium import webdriver
import  time
import unittest
import HTMLTestRunner

class Nala(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.test_url="http://www.nala.com.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.test_url)
        #driver.find_element_by_css_selector(".red").click()
        driver.find_element_by_class_name("red").click()
        driver.find_element_by_css_selector("input[name='userName']").send_keys("18267200735")
        driver.find_element_by_css_selector("input[name='password']").send_keys("hj123456")
        driver.find_element_by_css_selector("input[type='submit']").click()
        loginName= driver.find_element_by_css_selector(".gold").text
        print loginName

        try:
            self.assertEqual(loginName,'18267200736',msg='error')

        except:
            print('what the fuck !')

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":

    suit = unittest.TestSuite()

    suit.addTest(Nala('test_login'))

    filename= 'F:\\Github\\Selenium-python\\Report\\nalalogin.html'

    fp=open(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='nalatestlogin',description='testreport')

    runner.run(suit)

    fp.close()









