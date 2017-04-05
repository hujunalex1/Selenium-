#coding=utf-8
from selenium import webdriver


#实例化一个火狐配置文件
fp = webdriver.FirefoxProfile()


#设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。

#设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
fp.set_preference("browser.download.folderList",2)


#是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
fp.set_preference("browser.download.manager.showWhenStarting",False)


#下载到指定目录
fp.set_preference("browser.download.dir","c:\\Temp")


#不询问下载路径；后面的参数为要下载页面的Content-type的值
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")


#启动一个火狐浏览器进程，以刚才的浏览器参数
driver = webdriver.Firefox(firefox_profile=fp)

#打开下载页面
driver.get("https://pypi.python.org/pypi/selenium")


#点击某个按钮
driver.find_element_by_xpath("//*[@id='content']/div[3]/table/tbody/tr[2]/td[1]/span").click()


#如果是某个直接下载链接，则缺少了点击某个链接或者按钮的操作，打开页面后执行下载动作


