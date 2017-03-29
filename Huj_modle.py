from time import sleep

from selenium.webdriver.support.select import Select


class RanzhiLib():
    # 构造方法
    def __init__(self, driver):
        self.driver = driver

    # 模块化添加用户
    def add_user(self, user):
        driver = self.driver
        # 添加用户名
        ac = driver.find_element_by_id('account')
        ac.send_keys(user['account'])
        # 真实姓名
        rn = driver.find_element_by_id('realname')
        rn.clear()
        rn.send_keys(user['realname'])
        # 选择性别
        if user['gender'] == 'm':
            driver.find_element_by_id('gender2').click()
        elif user['gender'] == 'f':
            driver.find_element_by_id('gender1').click()
        # 选择部门
        dp = driver.find_element_by_id('dept')
        Select(dp).select_by_index(user['dept'])
        # 选择角色
        role = driver.find_element_by_id('role')
        Select(role).select_by_index(user['role'])
        # 输入密码
        pwd1 = driver.find_element_by_id('password1')
        pwd1.clear()
        pwd1.send_keys(user['password'])

        pwd2 = driver.find_element_by_id('password2')
        pwd2.send_keys(user['password'])
        # 输入邮箱
        em = driver.find_element_by_id('email')
        em.send_keys(user['email'])
        # 点击保存
        driver.find_element_by_id('submit').click()
        sleep(2)

    # 登录账号
    def logn_in(self, name, password):
        driver = self.driver
        driver.get('http://localhost:8080/ranzhi/www')
        sleep(2)

        driver.find_element_by_id('account').clear()
        driver.find_element_by_id('account').send_keys(name)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('submit').click()
        sleep(2)

    # 退出账号
    def logn_out(self):
        self.driver.find_element_by_id('start').click()
        sleep(4)
        self.driver.find_element_by_link_text(u'退出').click()
        sleep(3)

    # 点击后台管理
    def click_admin_app(self):
        self.driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
        sleep(1)

    def click_add_user(self):
        self.driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a/h3').click()
        sleep(3)