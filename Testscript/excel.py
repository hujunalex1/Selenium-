#coding=utf-8


import  xlrd

ePath = "F:\\GitHub\\Selenium-python\\TestData\\test.xls"


xlBook = xlrd.open_workbook(ePath)

count = len(xlBook.sheets())
print "工作簿总数：",count


table = xlBook.sheets()[0]

rows = table.nrows
cols = table.ncols

print "行列为(%d,%d)" %(rows,cols)

for i in range(0,rows):
    rowValues = table.row_values(i)
    for data in rowValues:
        print  data, " "










