#!/usr/bin/env python
# coding=utf-8

"""
Created on 2019年07月20日
@author: zhangyp
describe：开票测试用例
"""
import os
from test_tools.utils.edit_file.read_ymal import Config
from test_tools.utils.edit_file.operation_excel import ExcelReader_Row_Litle, ExcelReader_Clo_Litle



# excel配置文件路劲
config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "test_ymal", "excel_ymal")
# 工程测试数据目录
testdata_projectdir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "test_data", "fpt-dsqz")


def get_excel_config_data(project):
    """
    根据配置文件，传入项目，获取项目测试数据文件，和每个sheet的name
    :param project:
    :return:
    """
    test_data_filename = Config(config_file).get(project).get("file_name")
    test_data_sheetdict = Config(config_file).get(project).get("sheet_name")
    prject_dict = {
        "test_data_filename": test_data_filename,
        "test_data_sheetdict": test_data_sheetdict,
    }
    return prject_dict


def get_test_data(project, api_name):
    """
    获取execel的测试数据
    :param project:
    :return:
    """
    print(type(api_name), api_name)
    prject_dict = get_excel_config_data(project)
    test_data_filename = prject_dict.get("test_data_filename")
    test_data_sheetdict = prject_dict.get("test_data_sheetdict")
    excelfile_dir = os.path.join(testdata_projectdir, test_data_filename)
    sheet_name = test_data_sheetdict.get(api_name)
    read_excel = ExcelReader_Row_Litle(excelfile_dir, sheet_name)
    api_test_data = read_excel.data()
    return api_test_data


def get_golble_data(project):
    """
    获取execel的公共参数
    :param project:
    :return:
    """
    prject_dict = get_excel_config_data(project)
    test_data_filename = prject_dict.get("test_data_filename")
    test_data_sheetdict = prject_dict.get("test_data_sheetdict")
    excelfile_dir = os.path.join(testdata_projectdir, test_data_filename)
    sheet_name = test_data_sheetdict.get("groble")
    read_excel = ExcelReader_Clo_Litle(excelfile_dir, sheet_name)
    api_test_data = read_excel.data()[0]
    return api_test_data



# a = get_test_data("fpt-dsqz", "open_bill")
# print(a)








