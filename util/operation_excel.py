# coding: utf-8
# @Time    : 2018/6/22 0022 上午 10:01
# @Author  : 许榕亭
# @File    : operation_excel.py
import xlrd


class OperationExcel:

    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../data_config/case1.xls'
        else:
            self.file_path = file_path
        self.excel = self.get_excel()

    def get_excel(self):
        """
        获取excel文件
        :return: excel文件
        """
        try:
            tables = xlrd.open_workbook(self.file_path)
            return tables
        except FileNotFoundError as e:
            print("程序异常", e)

    def get_sheet(self, i=None):
        """
        听过index获取sheet内容
        :return:sheet内容
        """
        if i is None:
            i = 0
        return self.excel.sheets()[i]

    def get_rows(self):
        """
        获取行数
        :return: 行数
        """
        return self.get_sheet().nrows

    def get_cell(self, row, col):
        return self.get_sheet().cell_value(row, col)


