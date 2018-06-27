# coding: utf-8
# @Time    : 2018/6/22 0022 上午 10:52
# @Author  : 许榕亭
# @File    : base_driver.py
import time

from selenium import webdriver
from util.get_by_locator import GetByLocator


class BaseDriver:
    def __init__(self):
        self.driver = None

    def open_browser(self, browser):
        """
        打开浏览器
        :param browser:浏览器类型
        """
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def get_url(self, *args):
        """
        输入url
        :param url: 地址
        """
        self.driver.get(args[0])

    def get_element(self, *args):
        """
        定位元素
        :return: 元素
        """
        return GetByLocator(self.driver).get_local_element(args[0])

    def element_send_keys(self, *args):
        """
        输入内容
        :param value: 元素定位信息
        :param text: 输入内容
        """
        self.get_element(args[0]).send_keys(args[1])

    def click_element(self, *args):
        """
        点击元素
        :param value: 元素定位信息
        """
        self.get_element(args[0]).click()

    def sleep_time(self, *args):
        time.sleep(2)

    def close_browser(self):
        self.driver.close()
