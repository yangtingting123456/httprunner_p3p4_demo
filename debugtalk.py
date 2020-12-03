#encoding=utf-8
import requests
import random
from faker import Faker
import pymysql

#获取商会网站登录的token
def get_access_token():
    json_data= {"name": "admin","password": "e10adc3949ba59abbe56e057f20f883e"}
    headers_data = {"Content-Type": "application/json"}
    try:
        response = requests.post(url='http://www.zhufu.juneyaokc.com/commerceapi/member/login',json=json_data,headers=headers_data)
        token = response.json()['data']['token']
    except KeyError as e:
        token = None
    return token
#定义获取关键字函数
def get_keyword():
    word_list = [' request','httprunner','ui',12306]
    num = random.randint(0,len(word_list)-1)
    return word_list[num]
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
    base_str = base_str +'!@#$%^&*()_<?'
    random_list = []
    for i in  range(count):
        str = ''
        for j in range(0,int(str_len)):
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

def get_random_int(a,b):
    return random.randint(a,b)

def get_random_name(count=5):
    f = Faker(locale='zh_CN')  # 文化设置,默认en_US
    name_phone_list = []
    for i in range(count):
        name_phone_list.append(f.name() + '手机号：' + f.phone_number())
    return name_phone_list
#链接数据库
def connmysql_params(name):
    conn =pymysql.connect(host ='192.168.177.42',port = 3306,user='root',
                          password='Php123&juneyaokc',
                          database='shfscc',charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute("SELECT name,password FROM member ;")
    names =cur.fetchall()
    cur.close()
    conn.close()
    return names
def to_iso8859(str):
    return str.encode('utf-8').decode('iso8859-1')

def to_utf_8(str):
    return str.encode("ISO-8859-1").decode("utf8")

if __name__ == '__main__':
    # result = connmysql_params('testsuit04.yml')
    # print(result)
    print(to_iso8859("_湖南新梦想软测教育咨询有限公司"))
    print(to_utf_8(" æ°æ¢¦æ³,æ°æ¢¦æ³IT,æ°æ¢¦æ³ITæè²,æ°æ¢¦æ³ITæè²å¹è®­,é¿æ²æ°æ¢¦æ³IT,"
                   "è½¯ä»¶æµè¯å¹è®­,é¿æ²è½¯ä»¶æµè¯å¹è®­,"
                   "é¿æ²javaå¹è®­,é¿æ²Pythonå¹è®­,é¿æ²ITå¹è®­,é¿æ²ITå¹è®­æºæ"))






