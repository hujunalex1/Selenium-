#coding:utf-8
import urllib
import urllib2
url="http://api.meizhuangdaka.com/app/user/info"
#定义请求数据
data = {}
data["androidchannel"] = "Lenovo"
data["sign"] = "b88f86bcec8bbb6e70bb25f956298a6b"
data["source"] = "android"
data["version"] = "1.5.0"
data["token"] = "af4ad705-7517-44df-b3cb-105d6b1e8175"
#对请求数据进行编码
data=urllib.urlencode(data)
#将数据和url传给服务端
request = urllib2.Request(url,data) #post方式
#打开请求，获取数据
requestResponse=urllib2.urlopen(request)
#读取获取的数据
ss= requestResponse.read()
#打印数据
print ss
