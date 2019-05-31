#!/usr/bin/env python
# coding=utf-8
"""封装从测试用例获取数据的方法"""

from Common.util.get_dir import *
from Common.util.edit_file.edit_excel import *

test_data_excel = os.path.join(get_how_dir(os.path.abspath(__file__), 3), "data", "api_data.xlsx")


def get_golble_agrs():
    """获取excel中的全局参数，返回dict方便获取"""
    key_list = get_col_to_list(test_data_excel, "project_peizhi", 0)
    value_list = get_col_to_list(test_data_excel, "project_peizhi", 1)
    golble_dict = dict(zip(key_list, value_list))
    return golble_dict


def get_testcase_dict():
    test_case_dict = read_excel_to_dict(test_data_excel, "api_peizhi")
    return test_case_dict

