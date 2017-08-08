#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import traceback
# 'http': 'http://69bbf680.ngrok.io:808/'
# 'http': 'http://1r7523j220.51mypc.cn:33416/'
def test():
    proxies = {
        'http': 'http://0.tcp.ngrok.io:12459/'
    }
    headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    }
    print(proxies)
    try:
        response = requests.get('http://10.0.0.8/default2.aspx', proxies=proxies,headers=headers)
        print(response.text)
    except Exception as err:
        traceback.print_exc()
        print(err)
        input()
    print(response.status_code)
    input()
    # proxy_handler = urllib.request.ProxyHandler({'http': 'http://1r7523j220.51mypc.cn:33416/'})
    # opener = urllib.request.build_opener(proxy_handler)
    # r = opener.open('http://httpbin.org/ip')
    # print(r.read())

if __name__ == '__main__':
    # try:
    #     test()
    # except Exception as e:
    #     traceback.print_exc()
    #     err = traceback.format_exc()
    #     print(err)
    #     dir = os.getcwd() + "\\"
    #     try:
    #         with open(dir+"log.txt","w+") as t:
    #             t.write(err)
    #     except IOError:
    #         print("IO ERROR")
    #     finally:
    #         t.close()
        # print(e)
    test()
