import csv
import unittest
from time import sleep

from selenium import webdriver
# 模块化代码后引用需导入代码模块
from ranzhi_lib import RanzhiLib


class Ranzhi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lib = RanzhiLib(self.driver)

    # 主函数
    def test_ranzhi(self):
        # 读取CSV文件到user_list字典类型变量中
        user_list = csv.reader(open("list_to_user.csv", "r"))
        # 遍历整个user_list
        for user in user_list:
            sleep(2)
            self.lib.logn_in('admin', 'admin')
            sleep(2)
            # 断言
            self.assertEqual("http://localhost:8080/ranzhi/www/sys/index.html",
                             self.driver.current_url,
                             '登录跳转失败')
            # 读取一行csv，并分别赋值到user_to_add 中
            user_to_add = {'account': user[0],
                           'realname': user[1],
                           'gender': user[2],
                           'dept': user[3],
                           'role': user[4],
                           'password': user[5],
                           'email': user[0] + user[6]}
            # 点击后台管理
            self.lib.click_admin_app()
            # 进入嵌套
            self.lib.driver.switch_to.frame('iframe-superadmin')
            sleep(2)
            # 点击添加用户
            self.lib.click_add_user()
            # 添加用户
            self.lib.add_user(user_to_add)
            # 退出嵌套
            self.driver.switch_to.default_content()
            sleep(1)
            # 退出
            self.lib.logn_out()
            sleep(2)
            # 用新账号登录
            self.lib.logn_in(user_to_add['account'], user_to_add['password'])
            sleep(2)
            self.lib.logn_out()
            sleep(2)

    def tearDown(self):
        self.driver.quit()