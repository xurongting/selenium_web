# coding: utf-8
# @Time    : 2018/6/22 0022 上午 11:25
# @Author  : 许榕亭
# @File    : get_by_locator.py


class GetByLocator:
    def __init__(self, driver):
        self.driver = driver

    def get_local_element(self, key):
        key_split = key.split("=")
        by = key_split[0]
        value = key_split[1]
        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "link":
            return self.driver.find_element_by_link_text(value)
        elif by == "tag":
            return self.driver.find_element_by_tag_name(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            return self.driver.find_element_by_partial_link_text(value)
