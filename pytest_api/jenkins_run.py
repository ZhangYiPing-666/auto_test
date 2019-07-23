#!/usr/bin/env python
# coding=utf-8

"""
Created on 2019年07月20日
@author: zhangyp
describe：开票测试用例
"""

import os

test_path = os.path.join(os.path.dirname(__file__), "test_case")
test_data_path = os.path.join(os.path.dirname(__file__), "result")
test_report_path = os.path.join(os.path.dirname(__file__), "report")

os.system("pytest -s -q -n 2 %s --alluredir %s" % (test_path, test_data_path))
os.system("allure generate %s -o %s" % (test_data_path, test_report_path))
