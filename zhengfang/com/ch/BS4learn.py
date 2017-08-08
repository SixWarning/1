#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __mtime__ = '07/09'
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('new_file.html',encoding='utf-8'),'lxml')
open()
print(soup.p['class'][0][0])

# print("How old are you?")
# age = input()
# print("How tall are you?")
# height = input()
# print("How much do you weight?")
# weight = input()
# print(age + " " + height + " " + weight)
