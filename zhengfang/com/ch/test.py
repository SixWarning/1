#!/usr/bin/env python
#图文识别测试
# -*- coding: utf-8 -*-
# import requests
# url = "http://10.0.0.8/xs_main.aspx?xh=1522110408"
# headers = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Cookie":"ASP.NET_SessionId=znyk2p55m1go4pyrnzgkecny",
#     "Referer":"http://10.0.0.8/default2.aspx",
#      "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
# }
# r = requests.get(url,headers=headers)
#
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.text)

# r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
# print(r.url)
# print(r.text)   #打印解码后的返回数据

# import base64
# f=open('123.png','rb') #二进制方式打开图文件
# ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
# f.close()
# # img=Image.open("code.jpg")
# # vcode= pytesseract.image_to_string(img)
# print(ls_f)
import urllib
import urllib.parse
import urllib.request
import json

def api():
    host = 'http://ali-checkcode2.showapi.com'
    path = '/checkcode'
    method = 'POST'
    appcode = 'a0922771ab114d46a132c64ac391a411'
    querys = ''
    bodys = {}
    url = host + path

    bodys['convert_to_jpg'] = '0'
    bodys[
        'img_base64'] = '/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAYADwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD35twU7QC2OATgE1xPiTx3Jp+r6fpmg6dLrOqT273T2kciRxJACQXeY/KhDKQOSOoPJU12kTO8SNImxyoLJnO09xnvXmXiHQ/EGj+MrzxN4c0641NtVjjiu9Pa4W3KOihUkEo/g2ggpuB3EMcjAW4LXUmUZPZnUeFvGDeIHudOv9Nm0XXrYM0un3R3Ex7ioljbAEsZIxuXjPHQqTHB43hbx+/hKa1KzrFkXAfKu+wPtC44Gwk5J6jHPWuCi8SaxpnxRv8AXfFOl2+nzw+Fi0VlDP5pA+0qqq7qCNzSZ5GQFZc8g1QufEuiWXg6yvrDV0l8U297/akxNrIpmlk/1sZYYCrggNtIDCPpzVwhfoc9erySVnbr6o9O8OeMrTxnYS3eizraiCXypYr2EM+SBtOFk4ByQCepB9Kj8UeMItChGkLJFdeI7pEFpaqjxLKZH2Kd2SFwc9XBO3qMg1yHw6sbbwtrem2KPvtfEmjRXJMxDsbpBvaMBfup5chPzDnjB7VzWpJrPirxvYazZi2kOoXsr6PJJJIoMVpkgYz8queSDg7gT8gOTbir2W39f8EmVSShdfE/6/yPVPAt9d3GmNbXuqR3Wo2dzPbXybB99HIBXheCCpJwc57HNbf/AAkWjrxLqVvbv3iuX8mRfqj4YevI6c1wfwytdWnutd/tKCx+zDUbjzijOZVugUzg5xtAJwfvA55559IMDgARyYUDHzlmP57qwbVy4TqygmieuR1vw34gutQSXQvG91pR8oJJBNaxXalVJ2lQ2Cp+ZgWJJb5cn5aKKm9jptcytN+G0Jna7udc1G+kvLmK51c3kO37a8Q+RApACRAk/JhhjAyNoI7LX7CXVfDmqadAyLNdWksCM5IUMyFQTjPGTRRTUnoJwim/M4SX4Y6g/gfTNKTVbWPU9PjuFinWBipWdCJIjluhLEb9uQAMKDnO7qHh2ePxb4Ml061xpmkR3UUh8wfulaFUjHzHc3THf3ooq/aye/n+JCpRW3l+Bp2j6L4fvr+13QWLXM325zLccTPJkM3zHg5Q8DgDHrgbRcA4Ib8FJoop1YqMYyXUzozbco9n/mf/2Q=='
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
        print(json_data['showapi_res_body']['Result'])

if __name__ == '__main__':
    api();
