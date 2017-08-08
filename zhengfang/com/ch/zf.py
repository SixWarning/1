# __VIEWSTATE value="dDw3OTkxMjIwNTU7Oz6I0CdU+3X0rU9zcJxSpaxzgnaakg=="
# __VIEWSTATEGENERATOR  value="92719903"
#-*-coding:utf-8-*-
import os
import requests
from lxml import etree
import base64
import urllib
import urllib.parse
import urllib.request
import json
import traceback
httpNum = 'http://0.tcp.ngrok.io:12459/'
#图片转base64
def changebase64():
    f=open('code.jpg','rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    #print(ls_f)
    return ls_f

#验证码识别
def recognise(img_base64):
    host = 'http://ali-checkcode2.showapi.com'
    path = '/checkcode'
    method = 'POST'
    appcode = 'a0922771ab114d46a132c64ac391a411'
    querys = ''
    bodys = {}
    url = host + path

    bodys['convert_to_jpg'] = '0'
    bodys[
        'img_base64'] = img_base64
    bodys['typeId'] = '3040'
    post_data = urllib.parse.urlencode(bodys).encode(encoding='UTF8')
    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    # 根据API的要求，定义相对应的Content - Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read().decode(encoding='UTF8')
    json_data = json.loads(content)
    if (content):
        return json_data['showapi_res_body']['Result']


#登录正方系统
def loginZF(studentnumber,password):
    #访问正方
    session = requests.Session()
    #设置代理
    proxies = {
    'http': httpNum
    }
    session.proxies = proxies
    url = "http://10.0.0.8/default2.aspx?"
    response = session.get(url)
    print(response)
    #使用xpath获取__VIEWSTATE
    selector = etree.HTML(response.content)
    __VIEWSTATE = selector.xpath('//*[@id="form1"]/input[1]/@value')[0]
    __VIEWSTATEGENERATOR = selector.xpath('//*[@id="form1"]/input[2]/@value')[0]
    #print(__VIEWSTATE)
    #print(__VIEWSTATEGENERATOR)
    #取得验证码并下载到本地
    imgUrl = "http://10.0.0.8/CheckCode.aspx?"
    imgresponse = session.get(imgUrl, stream=True)
    #print(session.cookies)
    image = imgresponse.content
    DstDir = os.getcwd() + "\\" +"img" + '\\'
    #print("保存验证码在:" + DstDir + "code.jpg" + "\n输入验证码")
    try:
        with open(DstDir+"code.jpg","wb") as jpg:
            jpg.write(image)
    except IOError:
        exstr = traceback.format_exc()
        print(exstr)
        print("IO ERROR!")
        input()
    finally:
        jpg.close
    #手动输入验证码
    #code = input("请输入验证码：")#手输验证码
    img_base64 = changebase64();#图片转换base64编码
    code = recognise(img_base64)#转入图文识别
    #print(code)
    RadioButtonList1 = urllib.parse.quote(u'学生'.encode("gbk"))#将字符 转成请求头里需要的编码格式 url编码
    #print(RadioButtonList1)
    data = {
        "__VIEWSTATEGENERATOR":__VIEWSTATEGENERATOR,
        "RadioButtonList1":RadioButtonList1,
        "__VIEWSTATE":__VIEWSTATE,
        "TextBox1":studentnumber,
        "TextBox2":password,
        "TextBox3":code,
        "Button1":"",
    }
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    #print(data)

    #登陆教务系统
    response = session.post(url,data=data,headers=headers)
    #print(response.text)
    grade(response,studentnumber,session)


##获取学生姓名并编码，用于拼接请求地址
def getStudentname(response):
    selector = etree.HTML(response.content)
    studentname = selector.xpath('//*//em//span[@id="xhxm"]/text()')[:2][0]
    studentname = urllib.parse.quote(studentname.encode("gbk"))
    return studentname

#查询课程页面
def course(response,studentnumber,session):
    studentname = getStudentname(response)
    #拼接请求地址
    courseurl = "http://10.0.0.8/xskbcx.aspx?xh=" + studentnumber +"&xm=" + studentname + "gnmkdm=N121603"
    #构建请求头
    headers = {
        "Referer":"http://10.0.0.8/xs_main.aspx?xh="+studentnumber,
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    response = session.get(courseurl,headers=headers)
    html = response.content.decode("gb2312")
    print(html)

#访问成绩网站
def grade(response,studentnumber,session):
    studentname = getStudentname(response)
    #拼接请求头地址
    courseurl = "http://10.0.0.8/xscj.aspx?xh=" + studentnumber +"&xm=" + studentname + "gnmkdm=N121605"
    #构建请求头
    headers = {
        "Referer":"http://10.0.0.8/xscj.aspx?xh=" + studentnumber +"&xm=" + studentname + "gnmkdm=N121605",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    selector = etree.HTML(response.content)
    __VIEWSTATE = selector.xpath("//*[@id='Form1']/input[1]/@value")[0]
    __VIEWSTATEGENERATOR = selector.xpath('//*[@id="Form1"]/input[2]/@value')[0]
    ss = urllib.parse.quote("查询已修课程最高成绩".encode("gbk"))
    data = {
    "__VIEWSTATE":__VIEWSTATE,
    "__VIEWSTATEGENERATOR":__VIEWSTATEGENERATOR,
    "ddlXN":"",
    "ddlXQ":"",
    "txtQSCJ":0,
    "txtZZCJ":100,
    "Button6":ss
    }
    #发送请求
    responses = session.post(courseurl,headers=headers,data=data)
    grades = getGrades(responses)
    flag = 0
    for i in grades:
        flag += 1
        number = chinese(i)
        newStr = '{0:{wd}}'.format(i,wd=42-number)
        print('%s' % newStr,end="")
        flag = flag%4
        if(flag == 0):
            print()
    input()

def chinese(data):
    count = 0
    for s in data:
         if ord(s) > 127:
            count += 1
    return count

#获取分数的xpath
def getGrades(responses):
    selector = etree.HTML(responses.content)
    grades = selector.xpath('//table[@id="Datagrid3"]/tr/td/text()')
    return grades

if __name__ == '__main__':
    #初始参数
    studentnumber = input("请输入你的学号：")
    password = input("请输入你的密码：")
    try:
        loginZF(studentnumber,password)
        # loginZF()
    except Exception as e:
        traceback.print_exc()
        err = traceback.format_exc()
        print(err)
        dir = os.getcwd() + "\\"
        try:
            with open(dir+"log.txt","w+") as t:
                t.write(err)
        except IOError:
            print("IO ERROR")
        finally:
            t.close()
