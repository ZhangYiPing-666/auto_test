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
    """发票作废"""
    def setUp(self):
        pass

    def test_001(self):
        """普票--蓝票_已开作废:"""
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
        kj_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
        arrequt_respont_openbill(kj_res, "0000")
        zuofei_message = get_zuofei_message(kj_res, message_file, zuofei_type="1")
        zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
        arrequt_respont_zuofgei(zf_res, "0000")
    #
    # def test_002(self):
    #     """普票--红票_已开作废:"""
    #     change_message = {
    #         "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
    #         "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    #         "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
    #         "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
    #         "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
    #         "REQUEST_COMMON_FPKJ.YFP_HM": "",  # 原发票号码
    #         "REQUEST_COMMON_FPKJ.TZDBH": "",
    #         "REQUEST_COMMON_FPKJ.QDBZ": "0"
    #     }
    #     blue_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
    #     arrequt_respont_openbill(blue_res, "0000")
    #     print_log("蓝票开具成功\n\n")
    #     change_message = gengxin_red_message(blue_res, change_message)
    #     red_res = open_zhi_red_bill(API_data_file, api_name, blue_res["message"], change_message)
    #     arrequt_respont_openbill(red_res, "0000")
    #     print_log("红票开具成功")
    #     zuofei_message = get_zuofei_message(red_res, message_file, zuofei_type="1")
    #     zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
    #     arrequt_respont_zuofgei(zf_res, "0000")

    def test_003(self):
        """普票--未开作废:"""
        fplx = "007"
        res = get_now_dmhm(API_data_file, api_name, message_file, "search_weikai", fplx)
        arrequt_respont_getdh(res["res"], "0000")
        zuofei_message = get_zuofei_message(res, message_file, fplx=fplx, zuofei_type="0")
        zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
        arrequt_respont_zuofgei(zf_res, "0000")

    # def test_004(self):
    #     """专票--蓝票_已开作废:"""
    #     change_message = {
    #         "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
    #         "REQUEST_COMMON_FPKJ.FPLXDM": "004",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    #         "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
    #         "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
    #         "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
    #         "REQUEST_COMMON_FPKJ.YFP_HM": "",  # 原发票号码
    #         "REQUEST_COMMON_FPKJ.TZDBH": "",
    #         "REQUEST_COMMON_FPKJ.QDBZ": "0"
    #     }
    #     kj_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
    #     arrequt_respont_openbill(kj_res, "0000")
    #     zuofei_message = get_zuofei_message(kj_res, message_file, zuofei_type="1")
    #     zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
    #     arrequt_respont_zuofgei(zf_res, "0000")
    #
    # def test_005(self):
    #     """专票--红票_已开作废:"""
    #     change_message = {
    #         "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
    #         "REQUEST_COMMON_FPKJ.FPLXDM": "004",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    #         "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
    #         "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
    #         "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
    #         "REQUEST_COMMON_FPKJ.YFP_HM": "",  # 原发票号码
    #         "REQUEST_COMMON_FPKJ.TZDBH": "",
    #         "REQUEST_COMMON_FPKJ.QDBZ": "0"
    #     }
    #     bludkj_res = open_blue_zhi_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
    #     arrequt_respont_openbill(bludkj_res, "0000")
    #     sq_message = get_shengqi_message(bludkj_res, message_file, ZDBZ="0", YWLX="0")
    #     sq_res = zhuanshenqing_fapiao(API_data_file, api_name, sq_message)
    #     sh_res = shenhe_hongzi(bludkj_res, "tongguo")
    #     sq_message = get_shengqi_message(bludkj_res, message_file, ZDBZ="0", YWLX="1")
    #     sq_res = zhuanshenqing_fapiao(API_data_file, api_name, sq_message)
    #     response = type_to_json(decode_base64(jiexi_json(sq_res, "interface.Data.content")))
    #     change_message = gengxin_red_message(bludkj_res, change_message)
    #     change_message["REQUEST_COMMON_FPKJ.TZDBH"] = response["XXBBH"]
    #     red_res = open_zhi_red_bill(API_data_file, api_name, bludkj_res["message"], change_message)
    #     arrequt_respont_openbill(red_res, "0000")
    #     zuofei_message = get_zuofei_message(red_res, message_file, zuofei_type="1")
    #     zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
    #     arrequt_respont_zuofgei(zf_res, "0000")

    def test_006(self):
        """专票--未开作废:"""
        fplx = "004"
        res = get_now_dmhm(API_data_file, api_name, message_file, "search_weikai", fplx)
        arrequt_respont_getdh(res["res"], "0000")
        zuofei_message = get_zuofei_message(res, message_file, fplx=fplx, zuofei_type="0")
        zf_res = zuofei_fapiao(API_data_file, api_name, zuofei_message)
        arrequt_respont_zuofgei(zf_res, "0000")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

