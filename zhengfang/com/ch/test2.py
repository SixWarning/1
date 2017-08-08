#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '06/27'
import xlwt
import urllib,requests,json
def get_content(pn):
    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    items = []
    data = {
        'first':'true',
        'pn':pn,
        'kd':'python'
    }
    headers = {
        "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    html = requests.post(url,data=data,headers=headers).text
    html = json.loads(html)
    #print(html)
    for i in range(14):
        item = []
        item.append(html['content']['positionResult']['result'][i]['positionName'])#职位
        item.append(html['content']['positionResult']['result'][i]['companyFullName'])#公司名称
        item.append(html['content']['positionResult']['result'][i]['salary'])#薪资
        item.append(html['content']['positionResult']['result'][i]['city'])#地点
        item.append(html['content']['positionResult']['result'][i]['firstType'])#类型
        items.append(item)
    return items
#写入excel表
def excel_write(items):
    newTbale = 'text.xls' #表的名称
    wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，设置编码格式
    ws = wb.add_sheet('test1')#创建表的名称
    headdata = ['职位','公司名称','薪资','地点','类型']
    for hd in range(5):
        ws.write(0,hd,headdata[hd],xlwt.easyxf('font: bold on'))#0行，hd列,内容
        wb.save(newTbale)

    #把爬虫获取到的数据写入excel表
    index = 1
    for item in items :
        for i in range(5):
            ws.write(index,i,item[i])
        index += 1
        wb.save(newTbale)
if __name__ == '__main__':
    items = get_content(1)
    excel_write(items)
