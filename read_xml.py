#coding=utf-8

import xml.dom.minidom

#打开xml 文档
dom = xml.dom.minidom.parse("c:\\Temp\\info.xml")

#得到文档元素对象
root = dom.documentElement #documentElement 用于得到dom 对象的文档元素，并把获得的对象给root
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

"""
nodeName 为结点名字。
nodeValue 是结点的值，只对文本结点有效。
nodeType 是结点的类型。
"""
