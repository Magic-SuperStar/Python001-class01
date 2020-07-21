# -*- coding: utf-8 -*-
"""
author: LJZ
time: 2020/7/18 18:54

"""
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/login?from=home',
}
# https://shimo.im/lizard-api/auth/password/login
login_url = 'https://shimo.im/lizard-api/auth/password/login'

s = requests.Session()
from_data = {
    'email': '1318956704@qq.com',
    'mobile': '+86undefined',
    'password': '123456789',
}

response = s.post(login_url, data=from_data, headers=headers)
print(response.status_code)
resp=s.get('https://shimo.im/dashboard/used',headers=headers)
print(resp.status_code)
print(resp.text)
