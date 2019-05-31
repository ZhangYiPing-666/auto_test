#!/usr/bin/env python
# coding=utf-8


import unittest
from page.open_bill_common import *
from page.assert_resule import *


file = os.getcwd()

API_data_file = os.path.join(file,"case","case_data.yml")
api_name = "/fpt-cloudservice/invoice"
message_file = os.path.join(file,"case","pan","open_bill_message.yml")
search_message = "search_bill"
pan_file = os.path.join(file,"case","pan","panpeizhi.yml")



class open_bill():
    """盘接口-电票-正常流程--蓝票开票"""
    def __init__(self, pan):
        self.pan = pan

    def test_001(self):
        """蓝票_1行_明细:"""
        change_message = {
            "REQUEST_COMMON_FPKJ.SKP_NO": self.pan.get("盘号"),  # 税盘盘号
            "REQUEST_COMMON_FPKJ.SKP_LX": "",  # 税控盘类型:[1-税控盘；2-金税盘]
            "REQUEST_COMMON_FPKJ.FPQQLSH": "",  # 发票请求流水号
            "REQUEST_COMMON_FPKJ.FPLXDM": "",  # 发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
            "REQUEST_COMMON_FPKJ.KPLX": "",  # 开票类型:[0-蓝字发票； 1-红字发票]
            "REQUEST_COMMON_FPKJ.ZSFS": "",  # 征税方式:[0：普通征税,2：差额征税]
            "REQUEST_COMMON_FPKJ.XSF_NSRSBH": self.pan.get("税号"),  # 销售方纳税人识别号
            "REQUEST_COMMON_FPKJ.XSF_MC": self.pan.get("企业名称"),  # 销售方名称
            "REQUEST_COMMON_FPKJ.YFP_DM": "",  # 原发票代码
            "REQUEST_COMMON_FPKJ.YFP_HM": ""  # 原发票号码
        }
        blue_res = open_blue_bill(API_data_file, api_name, message_file, "blue_1_line",change_message)
        arrequt_respont_pan_openbill(blue_res, "0000")
        # time.sleep(30)
        # blue_result = deepcopy(blue_res)
        # response_search = search_bill(API_data_file, api_name, search_message, blue_result, self.pan)
        # result_search = get_respont_result(response_search)
        # try:
        #     assert_equare("0000", result_search.get("returnCode"))
        #     print_log("查询成功" + result_search.get("returnMessage"))
        #     debase64_result = get_debase64_bill_message(response_search)
        #     print_number(debase64_result)
        # except:
        #     e = "查询失败" + result_search.get("returnCode") + result_search.get("returnMessage")
        #     raise Exception(e)






class RunTest(unittest.TestCase):
    """蓝票开票"""

    def setUp(self):
        # panhao = ["5729","4045","4050","5690","5622","5614"]
        # panhao = ["5622", "5729", "5690", "5614"]
        panhao = ["4050", "4045"]
        self.pan_list = []
        for i in panhao:
            pan = Config(pan_file).get(i)
            self.pan_list.append(pan)


    def test_open(self):
        for i in range(1800):
            for pan in self.pan_list:
                print("\n","\n")
                try:
                    run = open_bill(pan)
                    run.test_001()
                    time.sleep(60)
                except Exception as e:
                    print_log(e)
                    continue



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

