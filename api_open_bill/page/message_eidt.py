#!/usr/bin/env python
# coding=utf-8
from util.operation_json import *
from util.encryption import *
from util.config import Config
from copy import deepcopy
from util.number import *
import requests
import os


huanjing_file = os.path.join(os.path.abspath(os.path.dirname("./")), "huanjing", "huanjing")
db_file = os.path.join(os.path.abspath(os.path.dirname("./")), "huanjing", "db_config")
huanjing_dict = Config(huanjing_file).get("use")
qianzhi_url = huanjing_dict.get("qianzhi_url")
pan_url = huanjing_dict.get("pan_url")
SECRET_KEY = huanjing_dict.get("key")
APP_id = huanjing_dict.get("appid")
xs_mc = huanjing_dict.get("XSF_MC")
xs_sbh = huanjing_dict.get("SKP_NO")
geshi_peizhi = huanjing_dict.get("geshi")
GMF_MC = huanjing_dict.get("GMF_MC")
KPZDBS = huanjing_dict.get("KPZDBS")
HSBZ = huanjing_dict.get("HSBZ")
db_peizhi = Config(db_file).get("skdata_0322")


def get_debase64_bill_message(res):
    """
    从响应结果中获取加密报文进行解密
    """
    response_base64 = jiexi_json(res,"interface.Data.content")
    response = decode_base64(response_base64)
    response = type_to_json(response)
    return response


def change_pan_search(message, pan):
    """修改查询报文的盘信息"""
    pan = dict(pan)
    message = get_new_json(message, "REQUEST_COMMON_FPCX.XSF_NSRSBH", pan.get("税号"))
    return message


def get_shengqi_message(bludkj_res, message_file, ZDBZ="0", YWLX="0"):
    """获取专票红冲报文"""
    sq_message = Config(message_file).get("zhuan_bill_hong_shenqing")
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.ZDBZ", ZDBZ)
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.YWLX", YWLX)
    response = type_to_json(decode_base64(jiexi_json(bludkj_res, "res.interface.Data.content")))
    kj_message = bludkj_res["message"]
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.NSRSBH", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.XSF_NSRSBH"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.KPZDDM", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.KPZDBS"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.FPLXDM", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.FPLXDM"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.XSF_NSRSBH", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.XSF_NSRSBH"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.XSF_MC", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.XSF_MC"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.GMF_NSRSBH", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.GMF_NSRSBH"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.GMF_MC", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.GMF_MC"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.YFP_DM", jiexi_json(response, "FP_DM"))
    sq_message = get_new_json(sq_message, "REQUEST_COMMON_HZFPSQ.YFP_HM", jiexi_json(response, "FP_HM"))
    return sq_message


def get_zuofei_message(res, message_file, fplx="", zuofei_type="1"):
    """获取纸票作废报文"""
    zf_message = Config(message_file).get("zuofei")
    zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.NSRSBH", xs_sbh)
    zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.KPZDBS", KPZDBS)
    zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FPLXDM", fplx)
    zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.ZFLX", zuofei_type)
    response = type_to_json(decode_base64(jiexi_json(res, "res.interface.Data.content")))
    if zuofei_type == "1":
        kj_message = res["message"]
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FPQQLSH", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.FPQQLSH"))
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FPLXDM",jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.FPLXDM"))
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.HJJE", jiexi_json(kj_message, "REQUEST_COMMON_FPKJ.HJJE"))
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FP_DM", jiexi_json(response, "FP_DM"))
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FP_HM", jiexi_json(response, "FP_HM"))
    else:
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FP_DM", jiexi_json(response, "DQFPDM"))
        zf_message = get_new_json(zf_message, "REQUEST_COMMON_FPZF.FP_HM", jiexi_json(response, "DQFPHM"))
    return zf_message


def get_openbill_FPQQLSH(res):
    """
    获取开票的流水号
    """
    FPQQLSH = jiexi_json(res["message"],"REQUEST_COMMON_FPKJ.FPQQLSH")
    return FPQQLSH


def pan_gengxin_red_message(res, changemessage, debase64_result):
    """
    获取红票的changemessage
    """
    res = res["res"]
    changemessage["REQUEST_COMMON_FPKJ.YFP_DM"] = debase64_result["FP_DM"]
    changemessage["REQUEST_COMMON_FPKJ.YFP_HM"] = debase64_result["FP_HM"]
    changemessage["REQUEST_COMMON_FPKJ.FPQQLSH"] = ""
    return changemessage


def inster_zhi_json(message_dict, value_dict):
    """
    增加纸票报文开具字段
    """
    mes_dict = deepcopy(message_dict)
    mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.KPZDBS", KPZDBS)
    mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.FPLXDM", value_dict["REQUEST_COMMON_FPKJ.FPLXDM"])
    mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.TZDBH", value_dict["REQUEST_COMMON_FPKJ.TZDBH"])
    mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.QDBZ", value_dict["REQUEST_COMMON_FPKJ.QDBZ"])
    mingxi_json = jiexi_json(mes_dict, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX")
    if isinstance(mingxi_json, dict):
        if "HSBZ" not in mingxi_json:
            mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.HSBZ", HSBZ)
    if isinstance(mingxi_json, list):
        mingxis = []
        for mingxi in list(mingxi_json):
            if "HSBZ" not in mingxi_json:
                mingxi["HSBZ"] = HSBZ
                mingxis.append(mingxi)
        mes_dict = inster_new_json(mes_dict, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX",
                                   mingxis)
    return mes_dict


def get_message(message_file, message_name, change_message, messages=""):
    """
    #读取配置文件获取message,根据change_message重新改写message，并返回
        change_message = {
    "REQUEST_COMMON_FPKJ.SKP_NO": "",                   #税盘盘号
    "REQUEST_COMMON_FPKJ.SKP_LX": "",                   #税控盘类型:[1-税控盘；2-金税盘]
    "REQUEST_COMMON_FPKJ.FPQQLSH": "",                  #发票请求流水号
    "REQUEST_COMMON_FPKJ.FPLXDM": "",                   #发票类型代码:[026 增值税普票(电票),004 增值税专票(纸票),007 增值税普票(纸票),025 增值税普票(卷票)]
    "REQUEST_COMMON_FPKJ.KPLX": "",                     #开票类型:[0-蓝字发票； 1-红字发票]
    "REQUEST_COMMON_FPKJ.ZSFS": "",                     #征税方式:[0：普通征税,2：差额征税]
    "REQUEST_COMMON_FPKJ.XSF_NSRSBH": "",               #销售方纳税人识别号
    "REQUEST_COMMON_FPKJ.XSF_MC": "",                   #销售方名称
    "REQUEST_COMMON_FPKJ.YFP_DM": "",                   #原发票代码
    "REQUEST_COMMON_FPKJ.YFP_HM": ""                    #原发票号码
    }
    """
    cha_message = change_message
    if messages != "":
        message = messages
    else:
        message = Config(message_file).get(message_name)
    lsh = "PPMM" + str(get_random_FPQQLSH_16())
    print(lsh)
    message = get_new_json(message, "REQUEST_COMMON_FPKJ.FPQQLSH", lsh)
    for k,v in cha_message.items():
        falg = key_excit_json(message, k)
        if falg and (v != ""):
            message = get_new_json(message, k, v)
    return message


def get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1001"):
    """
        格式化通用接口请求参数
    """
    appid = APP_id       # 通用appid
    key = SECRET_KEY                                                        # 通用key
    request_data = Config(api_file).get(api_name).get("data")                                 # 获取request
    now_time = str(get_time())
    request_data = get_new_json(request_data, "interface.globalInfo.requestTime", now_time)          # 修改请求时间
    request_data = get_new_json(request_data, "interface.globalInfo.interfaceCode", intefacecode)
    dataexchangeid = "DZFPQZDFXJ1001" + str(get_time_2()) + str(get_random_FPQQLSH_9())
    request_data = get_new_json(request_data, "interface.globalInfo.dataExchangeId", dataexchangeid) # 修改changeid
    request_data = get_new_json(request_data, "interface.globalInfo.appId", appid)                   # 修改appid为通用
    message_base64 = encode_base64(message)
    message_base64 = message_base64.replace("\n", "")           # 请求报文进行base64加密并去掉换行符
    request_data = get_new_json(request_data, "interface.Data.content", message_base64)     # 修改content字段
    contentkey = request_encryption(message, key)                                           # 调接口message进行加密
    request_data = get_new_json(request_data, "interface.Data.contentKey", contentkey)      # 修改contentkey字段
    return request_data


def request_encryption(message, key):
    """
        调接口将报文进行加密
    """
    url = "http://192.168.71.36:8080/testinteface/test_createContentKey.action"
    method = "POST"
    data = {
        'xml': message,
        'contentPassword': key
    }
    response = requests.request(method, url, data=data).text
    return response


def gengxin_red_message(res, changemessage):
    """
    获取红票的changemessage
    """
    res = res["res"]
    changemessage["REQUEST_COMMON_FPKJ.YFP_DM"] = get_debase64_bill_message(res).get("FP_DM")
    changemessage["REQUEST_COMMON_FPKJ.YFP_HM"] = get_debase64_bill_message(res).get("FP_HM")
    changemessage["REQUEST_COMMON_FPKJ.FPQQLSH"] = ""
    return changemessage


def response_into_json(response):
    """
    将数据格式转换为json
    :param response:
    :return:
    """
    if response[0] == "{":  # 字符串转换json
        response = json.loads(response)
    elif response[0] == "<":  # xml转换json
        xml = xmltodict.parse(response)
        response = json.dumps(xml, indent=1)
        response = json.loads(response)
        response = response["RESPONSE"]
    else:
        response = None
    return response
