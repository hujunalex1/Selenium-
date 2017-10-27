#coding=utf-8

import csv #导入csv 包


#读取本地CSV 文件
my_file = "c:\\Temp\\user.csv"
date = csv.reader(file(my_file,"rb"))


#循环输出每一行信息
for user in date:
    print user
