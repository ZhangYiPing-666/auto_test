#!/usr/bin/env python
# coding=utf-8


from page.open_bill_common import *
import unittest
from page.assert_resule import *

file = os.getcwd()

API_data_file = os.path.join(file,"case","case_data.yml")
api_name = "/fpt-cloudservice/invoice"
search_message = "search_bill"

message_file = os.path.join(file,"case","pan","open_bill_message.yml")

pan_file = os.path.join(file,"case","pan","panpeizhi.yml")
pan = Config(pan_file).get("use_pan")


class RunTest(unittest.TestCase):
    """盘接口-电票-优惠政策_免税--开票"""
    def setUp(self):
        pass

    def test_001(self):
        """优惠政策_免税_蓝票_1行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_免税_1_line",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("蓝票开具成功\n\n")

    def test_002(self):
        """优惠政策_免税_红票_1行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_免税_1_line",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("蓝票开具成功\n\n")

    def test_003(self):
        """优惠政策_免税_LSLBZ:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_免税_LSLBZ",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("蓝票开具成功\n\n")

    def test_004(self):
        """优惠政策_不征税_蓝票_1行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_不征税_1_line",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)
        print_log("蓝票开具成功\n\n")

    def test_005(self):
        """优惠政策_不征税_LSLBZ:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_不征税_LSLBZ",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)

    def test_006(self):
        """优惠政策_零税率_1_line:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_零税率_1_line",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)

    def test_007(self):
        """优惠政策_零税率_LSLBZ:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "优惠政策_零税率_LSLBZ",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        blue_result = deepcopy(blue_res)
        response_search = while_search(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        try:
            assert_equare("0000", result_search.get("returnCode"))
            print_log("查询成功" + result_search.get("returnMessage"))
            debase64_result = get_debase64_bill_message(response_search)
            print_number(debase64_result)
        except:
            e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
            raise Exception(e)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

