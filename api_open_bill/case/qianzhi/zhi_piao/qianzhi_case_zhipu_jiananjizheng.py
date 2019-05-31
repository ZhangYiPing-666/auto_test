#!/usr/bin/env python
# coding=utf-8


from page.open_bill_common import *
import unittest
from page.assert_resule import *

file = os.getcwd()

API_data_file = os.path.join(file,"case","case_data.yml")
message_file = os.path.join(file,"case","qianzhi","open_bill_message.yml")
api_name = "/fpt-dsqz/invoice"

# test_data = Config(API_data_file).get(api_name)


class RunTest(unittest.TestCase):
    """服务器接口--普票--减按计征--开票"""
    def setUp(self):
        pass

    def test_001(self):
        """蓝票_1行_明细_减按计征:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": "",  # 原发票号码
            "REQUEST_COMMON_FPKJ.TZDBH": "",
            "REQUEST_COMMON_FPKJ.QDBZ": "0"
        }
        blue_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "减按计征_正常税率",change_message)
        arrequt_respont_openbill(blue_res, "0000")

    def test_002(self):
        """红票_1行_明细_减按计征:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": "",  # 原发票号码
            "REQUEST_COMMON_FPKJ.TZDBH": "",
            "REQUEST_COMMON_FPKJ.QDBZ": "0"
        }
        blue_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "减按计征_正常税率",change_message)
        arrequt_respont_openbill(blue_res, "0000")
        print_log("蓝票开具成功\n\n")
        change_message = gengxin_red_message(blue_res, change_message)
        red_res = open_zhi_red_bill(API_data_file, api_name, blue_res["message"], change_message)
        arrequt_respont_openbill(red_res, "0000")
        print_log("红票开具成功")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

