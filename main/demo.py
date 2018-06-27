# coding: utf-8
# @Time    : 2018/6/13 0013 下午 3:43
# @Author  : 许榕亭
# @File    : demo.py
from selenium import webdriver
driver = webdriver.Chrome()
url = "https://www.imooc.com/"
driver.get(url)
driver.find_element_by_link_text("登录").click()
driver.close()
