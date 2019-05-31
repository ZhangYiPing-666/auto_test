#!/usr/bin/env python
# coding=utf-8

import time
import unittest
from util.HTMLTestRunner123 import HTMLTestRunner
# from util.mail import Email
from util.get_dir import *
import os

pwd = get_pwd()
REPORT_PATH = os.path.join(pwd, "report")


class EcshopTestRunner(object):
    case_path = os.path.join(pwd, "case")         # 执行全部用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*qianzhi_case_dian_open_blue_bill_testcase*.py")


if __name__ == '__main__':
        discover = EcshopTestRunner.discover
        report_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        report = REPORT_PATH + r"\goupiao%s.html" % report_time
        with open(report, 'wb') as f:
            runner =HTMLTestRunner(f,title='接口开票回归测试', description='验证开票接口功能')
            runner.run(discover)
        # e = Email(title='生产环境开票接口自动化测试',
        #           message='生产环境开票接口测试报告，请查收！',
        #           receiver=['zhangyp@fapiao.com','liuyl@fapiao.com'],
        #           server="smtp.163.com",
        #           sender="18420162846@163.com",
        #           password="zhangyiping520",
        #           path=report
        #           )
        # e.send()


