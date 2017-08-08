#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '07/03'
import  urllib.request
import  urllib
# str = "陈灏"
# str = urllib.parse.quote(str.encode("gbk"))
# print(str)
str = "%B2%E9%D1%AF%D2%D1%D0%DE%BF%CE%B3%CC%D7%EE%B8%DF%B3%C9%BC%A8"
str = str.encode("gbk")
ss = urllib.parse.quote("查询已修课程最高成绩".encode("gbk"))
print(ss)
