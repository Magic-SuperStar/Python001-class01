# -*- coding: utf-8 -*-
"""
author: LJZ
time: 2020/7/18 20:12

"""
from selenium import webdriver as wb
import time

try:
    browser = wb.Chrome()
    browser.get('https://shimo.im/welcome')
    time.sleep(1)
    # //*[@id="homepage-header"]/nav/div[3]/a[2]
    btn = browser.find_element_by_xpath('//div[@class="entries"]/a[@href="/login?from=home"]')
    btn.click()
    time.sleep(10)
    iemail = browser.find_element_by_xpath('//div[@class="input"]/input[@name="mobileOrEmail"]')
    ipassword = browser.find_element_by_xpath('//div[@class="input"]/input[@name="password"]')
    summit_btn = browser.find_element_by_xpath('//button[contains(@class,"sm-button submit sc")]')
    iemail.send_keys('1318956704@qq.com')
    ipassword.send_keys('123456789')
    summit_btn.click()
    # print(browser.page_source)
except Exception as e:
    print(e)
finally:
    browser.close()
