#encoding=utf-8
import requests
import random
#获取商会网站登录的token
def get_access_token():
    json_data= {"name": "admin","password": "e10adc3949ba59abbe56e057f20f883e"}
    headers_data = {"Content-Type": "application/json"}
    response = requests.post(url='http://dev.commerce.juneyaokc.com:8081/member/login',json=json_data,headers=headers_data)
    token = response.json()['data']['token']
    return token
#定义获取关键字函数
def get_keyword():
    keys = [' request','httprunner','ui',12306]
    for i in range(0,len(keys)-1):
        return keys[i]


