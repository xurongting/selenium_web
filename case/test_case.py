# coding: utf-8
# @Time    : 2018/6/22 0022 下午 1:53
# @Author  : 许榕亭
# @File    : test_case.py
from util.operation_excel import OperationExcel
from base.base_driver import BaseDriver


class TestCase:
    def __init__(self):
        self.opera_execl = OperationExcel()
        self.base_driver = BaseDriver()

    def run_main(self):
        row_num = self.opera_execl.get_rows()
        for i in range(1, row_num):
            is_run = self.opera_execl.get_cell(i, 2)
            if is_run == "no":
                method = self.opera_execl.get_cell(i, 3)
                opera = self.opera_execl.get_cell(i, 4)
                send_value = self.opera_execl.get_cell(i, 5)
                self.run_method(method, opera, send_value)

    def run_method(self, method, opera, send_value):
        base_driver_function = getattr(self.base_driver, method)
        if send_value == "":
            if opera == "":
                base_driver_function()
            else:
                base_driver_function(opera)
        else:
            base_driver_function(opera, send_value)


if __name__ == "__main__":
    test = TestCase()
    test.run_main()
