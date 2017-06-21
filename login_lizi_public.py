# coding=utf-8
from  selenium import webdriver
from public import login
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www-test.lizi.com"
        self.driver.implicitly_wait(5)

    def test_lizi(self):
        driver = self.driver
        driver.get(self.base_url)
        # 调用登录函数
        login.login(driver)
        text = driver.find_element_by_css_selector('.name').text
        print text
        self.assertEqual(text, u"被风吹过的夏天", msg="error")
        # 调用退出函数
        login.logout(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
