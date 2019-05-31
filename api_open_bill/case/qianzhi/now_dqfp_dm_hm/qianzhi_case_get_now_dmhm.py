#!/usr/bin/env python
# coding=utf-8


from page.open_bill_common import *
import unittest
from page.assert_resule import *

file = os.getcwd()

API_data_file = os.path.join(file, "case", "case_data.yml")
message_file = os.path.join(file, "case", "qianzhi", "open_bill_message.yml")
api_name = "/fpt-dsqz/invoice"


class RunTest(unittest.TestCase):
    """获取当前纸票票号"""
    def setUp(self):
        pass

    def test_001(self):
        """获取当前普票票号:"""
        fplx = "007"
        res = get_now_dmhm(API_data_file, api_name, message_file, "search_weikai", fplx)
        arrequt_respont_getdh(res["res"], "0000")

    def test_002(self):
        """获取当前专票票号:"""
        fplx = "004"
        res = get_now_dmhm(API_data_file, api_name, message_file, "search_weikai", fplx)
        arrequt_respont_getdh(res["res"], "0000")

    def test_003(self):
        """获取当前电票票号:"""
        fplx = "025"
        res = get_now_dmhm(API_data_file, api_name, message_file, "search_weikai", fplx)
        arrequt_respont_getdh(res["res"], "0000")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

