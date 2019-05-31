#!/usr/bin/env python
# coding=utf-8


from page.open_bill_common import *
import unittest
from copy import deepcopy
from page.assert_resule import *

file = os.getcwd()

API_data_file = os.path.join(file,"case","case_data.yml")
fuwu_message_file = os.path.join(file,"case","qianzhi","open_bill_message.yml")
fuwu_api_name = "/fpt-dsqz/invoice"



pan_api_name = "/fpt-cloudservice/invoice"
search_message = "search_bill"
pan_message_file = os.path.join(file,"case","pan","open_bill_message.yml")
pan_file = os.path.join(file,"case","pan","panpeizhi.yml")
pan = Config(pan_file).get("use_pan")


class RunTest(unittest.TestCase):
    """pan接口--开票--流水号已存在"""
    def setUp(self):
        pass

    # def test_001(self):
    #     """用服务器开过的电票流水号--进行pan开电票:"""
    #     change_message = {
    #         "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
    #         "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
    #         "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
    #         "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    #         "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
    #         "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
    #         "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
    #         "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
    #         "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
    #         "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
    #     }
    #     res001 = open_blue_bill(API_data_file, fuwu_api_name, fuwu_message_file, "blue_1_line", change_message)
    #     arrequt_respont_openbill(res001, "0000")
    #     print_log("第一次开票成功")
    #     change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
    #     res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
    #     arrequt_respont_pan_openbill(res002, "9990")
    #
    # def test_002(self):
    #     """用服务器开过的电票流水号--进行pan开纸票:"""
    #     change_message = {
    #         "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
    #         "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
    #         "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
    #         "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    #         "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
    #         "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
    #         "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
    #         "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
    #         "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
    #         "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
    #     }
    #     res001 = open_blue_bill(API_data_file, fuwu_api_name, fuwu_message_file, "blue_1_line", change_message)
    #     arrequt_respont_openbill(res001, "0000")
    #     print_log("第一次开票成功")
    #     change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
    #     res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
    #     arrequt_respont_pan_openbill(res002, "9990")

    def test_003(self):
        """用pan开过的电票流水号--进行盘开纸票:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res001 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res001, "0000")
        time.sleep(26)
        blue_result = deepcopy(res001)
        response_search = search_bill(API_data_file, pan_api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("第一次开票成功")
        change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
        change_message["REQUEST_COMMON_FPKJ.FPLXDM"] = "007"
        res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res002, "9990")

    def test_004(self):
        """用pan开过的纸票流水号--进行盘开电票:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res001 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res001, "0000")
        time.sleep(26)
        res001_result = deepcopy(res001)
        response_search = search_bill(API_data_file, pan_api_name, search_message, res001_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("第一次开票成功")
        change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
        change_message["REQUEST_COMMON_FPKJ.FPLXDM"] = "026"
        res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res002, "9990")

    def test_005(self):
        """用pan开过的电票流水号--进行盘开电票:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res001 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res001, "0000")
        time.sleep(26)
        blue_result = deepcopy(res001)
        response_search = search_bill(API_data_file, pan_api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("第一次开票成功")
        change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
        res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res002, "9990")

    def test_006(self):
        """用pan开过的纸票流水号--进行盘开纸票:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": pan.get("类型"),  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "007",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        res001 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res001, "0000")
        time.sleep(26)
        blue_result = deepcopy(res001)
        response_search = search_bill(API_data_file, pan_api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("第一次开票成功")
        change_message["REQUEST_COMMON_FPKJ.FPQQLSH"] = get_openbill_FPQQLSH(res001)
        res002 = open_blue_bill(API_data_file, pan_api_name, pan_message_file, "blue_1_line", change_message)
        arrequt_respont_pan_openbill(res002, "9990")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

