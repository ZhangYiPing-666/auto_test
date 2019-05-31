#!/usr/bin/env python
# coding=utf-8


from page.open_bill_common import *
from page.assert_resule import *
import unittest

file = os.getcwd()

API_data_file = os.path.join(file,"case","case_data.yml")
message_file = os.path.join(file,"case","qianzhi","open_bill_message.yml")
api_name = "/fpt-dsqz/invoice"

# test_data = Config(API_data_file).get(api_name)


class RunTest(unittest.TestCase):
    """服务器接口--电票--正常流程--蓝票开票"""
    def setUp(self):
        pass

    def test_001(self):
        """蓝票_1行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": "",  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": "",  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": "",  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res = open_blue_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
        arrequt_respont_openbill(res, "0000")

    def test_002(self):
        """蓝票_5行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": "",  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税1：减按计征2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": "",  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": "",  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res = open_blue_bill(API_data_file, api_name, message_file, "blue_5_line",change_message)
        arrequt_respont_openbill(res, "0000")

    def test_003(self):
        """蓝票_1页_清单:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": "",  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税1：减按计征2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": "",  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": "",  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res = open_blue_bill(API_data_file, api_name, message_file, "blue_1_pagelist",change_message)
        arrequt_respont_openbill(res, "0000")

    def test_004(self):
        """蓝票_3页_清单:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": "",  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税1：减按计征2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": "",  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": "",  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res = open_blue_bill(API_data_file, api_name, message_file, "blue_3_pagelist",change_message)
        arrequt_respont_openbill(res, "0000")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

