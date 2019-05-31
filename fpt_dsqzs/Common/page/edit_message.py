#!/usr/bin/env python
# coding=utf-8
"""编辑报文，根据报文模板，封装一些编辑报文的方法"""
from Common.page.get_message_template import *
from Common.util.edit_file.edit_xml import *
from Common.page.get_excel import *
from Common.util.number import *
from Common.util.encryption import *


def updata_msg_tongyong(interfaceCode):
    """根据参数获取通用报文,返回字符串报文"""
    tongyong_msg = ""                                                       # 定义通用报文，格式字符串
    appId = get_golble_agrs().get("appId")                                 # 企业ID
    requestTime = get_time_3()                                              # 请求时间
    dataExchangeId = get_dataExchangeId(interfaceCode)               # 数据交换流水号
    content = "content"                                             # 内部报文besa64加密
    contentKey = "contentKey"                                       # 内部报文besa64加密 再 MD5 再 AES 加密
    message_template = get_msg_tongyong()
    updata_node_value(message_template, "appId", appId)
    updata_node_value(message_template, "interfaceCode", interfaceCode)
    updata_node_value(message_template, "requestTime", requestTime)
    updata_node_value(message_template, "dataExchangeId", dataExchangeId)
    updata_node_value(message_template, "content", content)
    updata_node_value(message_template, "contentKey", contentKey)
    tongyong_msg = xmlclass_to_str(message_template)  # 更新通用报文
    return tongyong_msg


def get_dataExchangeId(interfaceCode):
    message_template = get_msg_tongyong()
    requestCode = get_node_value(message_template, "requestCode")
    dataExchangeId = requestCode + interfaceCode + get_time_8() + get_random_FPQQLSH_9()
    return dataExchangeId


def updata_dp_kj_bule(dp_kj_dict):
    """根据传入的参数，智能组装电票开具报文"""
    dp_kj_msg = ""    # 定义开票报文，格式字符串
    message_template = get_msg_dp_kp()

    updata_node_value(message_template, "FPQQLSH", get_kp_lsh())

    updata_node_value(message_template, "XSF_NSRSBH", get_golble_agrs().get("XSF_NSRSBH"))
    updata_node_value(message_template, "XSF_MC", get_golble_agrs().get("XSF_MC"))
    updata_node_value(message_template, "XSF_DZDH", get_golble_agrs().get("XSF_DZDH"))
    updata_node_value(message_template, "XSF_YHZH", get_golble_agrs().get("XSF_YHZH"))

    updata_node_value(message_template, "GMF_NSRSBH", get_golble_agrs().get("GMF_NSRSBH"))
    updata_node_value(message_template, "GMF_MC", get_golble_agrs().get("GMF_MC"))
    updata_node_value(message_template, "GMF_DZDH", get_golble_agrs().get("GMF_DZDH"))
    updata_node_value(message_template, "GMF_YHZH", get_golble_agrs().get("GMF_YHZH"))
    updata_node_value(message_template, "GMF_SJH", get_golble_agrs().get("GMF_SJH"))
    updata_node_value(message_template, "GMF_DZYX", get_golble_agrs().get("GMF_DZYX"))

    updata_node_value(message_template, "KPR", get_golble_agrs().get("KPR"))
    updata_node_value(message_template, "SKR", get_golble_agrs().get("SKR"))
    updata_node_value(message_template, "FHR", get_golble_agrs().get("FHR"))

    KPLX = "KPLX";updata_node_value(message_template, "KPLX", KPLX)
    ZSFS = "ZSFS";updata_node_value(message_template, "ZSFS", ZSFS)

    # 根据dp_kj_dict参数组装明细

    JSHJ = "JSHJ"; updata_node_value(message_template, "JSHJ", JSHJ)
    HJJE = "HJJE"; updata_node_value(message_template, "HJJE", HJJE)
    HJSE = "HJSE"; updata_node_value(message_template, "HJSE", HJSE)
    KCE = "KCE"; updata_node_value(message_template, "KCE", KCE)

    BZ = "BZ"; updata_node_value(message_template, "BZ", BZ)

    TSPZ = "TSPZ"; updata_node_value(message_template, "TSPZ", TSPZ)

    size = "10"; updata_node_attribute(message_template, "COMMON_FPKJ_XMXXS", "size", size)
    dp_kj_msg = xmlclass_to_str(message_template)  # 更新通用报文
    return dp_kj_msg


def updata_dp_kj_red(dp_kj_dict, message_template):
    """根据传入的参数，智能组装电票开具报文"""
    YFP_DM = "";updata_node_value(message_template, "YFP_DM", YFP_DM)
    YFP_HM = "";updata_node_value(message_template, "YFP_HM", YFP_HM)


def get_kp_lsh():
    lsh_tt = get_golble_agrs().get("kplsh_taitou")
    lsh = get_random_FPQQLSH_16() + lsh_tt
    return lsh





