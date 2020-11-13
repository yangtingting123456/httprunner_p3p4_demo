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
#执行测试用例之前的工作
def setup(case_name):
    print("测试用例 %s 初始化工作"%case_name)
#执行测试用例之后的工作
def teardown(case_name):
    print("测试用例 %s 执行完毕，进行清理操作"%case_name)

#调用 debugtalk.py 中自定义的函数生成参数列表
def get_param_01():
    return ['httprunner','12306','火车票']

#生成随机数字
def get_random_param(min,max,count=3):
    random_list = []
    for i in range(count):
        random_list.append(random.randint(min,max))
    return random_list
#生成随机字符串
def get_random_string(base_str,str_len,count=3):
    random_list = []
    for i in  range(count):
        str = ''
        for j in range(0,str_len):
            str = str +base_str[random.randint(0,len(base_str)-1)]
        random_list.append(str)

    return random_list
#生成随机手机号
def get_random_phone(*mobile_num,count=3):
    phone_list = []
    for i in range(0,count):
        str_start = random.choice(mobile_num)
        str_end = ''.join(random.sample('0123456789',8))
        str_phone = str(str_start) + str_end
        phone_list.append(str_phone)
    return phone_list

if __name__ == '__main__':
    print(get_random_phone('155',count=6))
