#!/usr/bin/env python
# coding=utf-8

"""
Created on 2017年4月20日
@author: zhangyp
describe：开票测试用例
"""

import pytest
import allure
from test_tools.test_page.get_test_data import get_test_data


class TestClass:

    @pytest.mark.parametrize("data", get_test_data("fpt-dsqz", "open_bill"))
    def test_search(self, data):
        allure.attach('用例名称', data.get("case_no"))
        allure.attach('用例输出', data.get("case_name"))
        allure.attach('用例描述', data.get("输出值"))

    @pytest.mark.parametrize("data", get_test_data("fpt-dsqz", "open_bill"))
    def test_openbill(self, data):
        allure.attach('用例名称', data.get("case_no"))
        allure.attach('用例输出', data.get("case_name"))
        allure.attach('用例描述', data.get("输出值"))


if __name__ == '__main__':
    pytest.main("-q test_001.py")




