#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '07/09'
import docx
import os
from lxml import etree
import  requests
import urllib
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    response = urllib.request.urlopen(url)
    return response.read()

def save_imgs(folder,img_addrs):
    doc = docx.Document()
    for each in img_addrs:
        img = requests.get(each)
        print(img)
        img = img.content
        doc.add_picture(img)
    doc.save('test.docx')

def download_mm(img_addrs):
    folder='img'
    # os.mkdir(folder)
    os.chdir(folder)
    save_imgs(folder,img_addrs)

dir = os.getcwd() + '\\'
with open(dir +"new_file.html",'r',encoding="utf-8") as f:
    content =f.read()
tree = etree.HTML(content)
img_big = tree.xpath('//ul[@class="bigimg cloth_shoplist"]/li/a/img/@data-original')
img_small = tree.xpath('//ul[@class="bigimg cloth_shoplist"]/li//ul/li/a/img/@data-original')
price = tree.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p/span/text()')
title = tree.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="name"]/a/@title')
dian = tree.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="link"]/a/@title')
# for i in range(len(price)):
#     with open(dir + 'd.txt','a',encoding="utf-8") as f:
#         f.writelines(price[i]+','+title[i]+','+dian[i])
#         f.write('\n')
# save_imgs('img\\',img_big)
print(title)

