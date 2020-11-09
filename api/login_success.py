import requests

def get_token():
    host ='http://dev.commerce.juneyaokc.com:8081/member/login'
    params_data = {
        "name": "admin",
        "password": "e10adc3949ba59abbe56e057f20f883e"}
    headres_data = {" Content-Type": "application/json"}
    response = requests.post(url=host,json=params_data,headre = headres_data)
    return response

token = get_token()
print(token)
