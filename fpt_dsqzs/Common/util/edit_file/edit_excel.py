#!/usr/bin/env python
# coding=utf-8

import os
from xlrd import open_workbook


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data


def get_sheet_to_table(file, sheet):
    """根据excel文件和sheet参数获取table"""
    if os.path.exists(file):
        pass
    else:
        raise FileNotFoundError('文件不存在！')
    workbook = open_workbook(file)
    if type(sheet) not in [int, str]:
        raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(sheet)))
    elif type(sheet) == int:
        table = workbook.sheet_by_index(sheet)
    else:
        table = workbook.sheet_by_name(sheet)
    return table


def read_excel_to_twolist(file, sheet):
    """将excel表格数据读取成二维数组"""
    _data = list()
    s = get_sheet_to_table(file, sheet)
    for col in range(0, s.nrows):
        # 遍历所有行，拼到self._data中
        _data.append(s.row_values(col))
    return _data


def read_excel_to_dict(file, sheet):
    """将excel表格数据根据表头生成dict"""
    _data = list()
    s = get_sheet_to_table(file, sheet)
    title = s.row_values(0)  # 首行为title
    for col in range(1, s.nrows):
        # 依次遍历其余行，与首行组成dict，拼到self._data中
        _data.append(dict(zip(title, s.row_values(col))))
    return _data


def get_row_to_list(file, sheet, row):
    """获取excel某一行的数据"""
    s = get_sheet_to_table(file, sheet)
    rows = s.row_values(row)
    return rows


def get_col_to_list(file, sheet, col):
    """获取excel某一列的数据"""
    s = get_sheet_to_table(file, sheet)
    cols = s.col_values(col)
    return cols