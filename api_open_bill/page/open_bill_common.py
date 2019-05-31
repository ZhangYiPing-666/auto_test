#!/usr/bin/env python
# coding=utf-8
"""
封装一些方法，用来操作message
"""

from util.connect_db import OperationMysql
from page.message_eidt import *
from util.operation_json import *
from util.get_dir import *
from util.print_result import *

huanjing_file = os.path.join(os.path.abspath(os.path.dirname("./")), "huanjing", "huanjing")
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
db_file = os.path.join(os.path.abspath(os.path.dirname("./")), "huanjing", "db_config")
db_peizhi = Config(db_file).get("skdata_0322")


def get_request_data_message_xml(api_file, api_name, messages):
    """
        读取配置文件获取requestdata,更新一些参数，根据通用key将messages进行加密，并返回
    """
    appid = APP_id       # 通用appid
    key = SECRET_KEY                                                        # 通用key
    request_data = Config(api_file).get(api_name).get("data")                                 # 获取request
    now_time = str(get_time())
    request_data = get_new_json(request_data, "interface.globalInfo.requestTime", now_time)          # 修改请求时间
    dataexchangeid = "DZFPQZDFXJ1001" + str(get_time_2()) + str(get_random_FPQQLSH_9())
    request_data = get_new_json(request_data, "interface.globalInfo.dataExchangeId", dataexchangeid) # 修改changeid
    request_data = get_new_json(request_data, "interface.globalInfo.appId", appid)                   # 修改appid为通用
    message = messages
    message = dict_to_json(message)                            # 修改请求报文为json格式
    message_base64 = encode_base64(message)
    message_base64 = message_base64.replace("\n", "")           # 请求报文进行base64加密并去掉换行符
    request_data = get_new_json(request_data, "interface.Data.content", message_base64)     # 修改content字段
    contentkey = request_encryption(message, key)                                           # 调接口message进行加密
    request_data = get_new_json(request_data, "interface.Data.contentKey", contentkey)      # 修改contentkey字段
    return request_data


def open_blue_bill(api_file, api_name, messages_file, messagename, changemessag, geshi=geshi_peizhi):
    """
        读取配置文件获取请求地址、请求参数，根据通用key将messages进行加密，并返回
    """
    changemessage = deepcopy(changemessag)
    changemessage["REQUEST_COMMON_FPKJ.GMF_MC"] = GMF_MC
    if "dsqz" in api_name:
        changemessage["REQUEST_COMMON_FPKJ.XSF_MC"] = xs_mc
        changemessage["REQUEST_COMMON_FPKJ.XSF_NSRSBH"] = xs_sbh
        url = qianzhi_url
    else:
        url = pan_url
    genxin_message = get_message(messages_file, messagename, changemessage)
    if geshi == "xml":
        message = str(jsonToXml(genxin_message))
    else:
        message = dict_to_json(genxin_message)
    request_data_dict = get_request_data_message_json(api_file, api_name, message)
    test_data = dict(Config(api_file).get(api_name))
    url = url
    method = test_data.get("method")
    if geshi=="xml":
        request_data = jsonToXml(request_data_dict)
        headers = {"Content-Type":"text/xml"}
    else:
        request_data = json.dumps(request_data_dict)
        headers = {"Content-Type": "application/json"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(1)
    res = type_to_json(res)
    response_dict = {
        "res":res,
        "message":genxin_message,
        "request_data":request_data_dict
    }
    return response_dict


def open_blue_zhi_bill(api_file, api_name, messages_file, messagename, changemessag, geshi=geshi_peizhi):
    """
        读取配置文件获取请求地址、请求参数，根据通用key将messages进行加密，并返回
    """
    changemessage = deepcopy(changemessag)
    changemessage["REQUEST_COMMON_FPKJ.GMF_MC"] = GMF_MC
    if "dsqz" in api_name:
        changemessage["REQUEST_COMMON_FPKJ.XSF_MC"] = xs_mc
        changemessage["REQUEST_COMMON_FPKJ.XSF_NSRSBH"] = xs_sbh
        url = qianzhi_url
    else:
        url = pan_url
    genxin_message = get_message(messages_file, messagename, changemessage)
    zhi_message = inster_zhi_json(genxin_message, changemessage)
    if geshi == "xml":
        message = str(jsonToXml(zhi_message))
    else:
        message = dict_to_json(zhi_message)
    request_data_dict = get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1009")
    test_data = dict(Config(api_file).get(api_name))
    url = url
    method = test_data.get("method")
    if geshi == "xml":
        request_data = jsonToXml(request_data_dict)
        headers = {"Content-Type":"text/xml"}
    else:
        request_data = json.dumps(request_data_dict)
        headers = {"Content-Type": "application/json"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(1)
    res = type_to_json(res)
    response_dict = {
        "res": res,
        "message": zhi_message,
        "request_data": request_data_dict
    }
    return response_dict


def open_red_bill(api_file, api_name, message, changemessag, geshi=geshi_peizhi):
    """
        红票开票，先开蓝票，获取代码号码
    """
    changemessage = deepcopy(changemessag)
    if "dsqz" in api_name:
        changemessage["REQUEST_COMMON_FPKJ.XSF_MC"] = xs_mc
        changemessage["REQUEST_COMMON_FPKJ.XSF_NSRSBH"] = xs_sbh
        url = qianzhi_url
    else:
        url = pan_url
    message = get_message("", "", changemessage, messages=message)
    genxin_message = blue_to_red(message)
    if geshi == "xml":
        message = str(jsonToXml(genxin_message))
    else:
        message = dict_to_json(genxin_message)
    request_data_dict = get_request_data_message_json(api_file, api_name, message)
    test_data = dict(Config(api_file).get(api_name))
    url = url
    method = test_data.get("method")
    if geshi=="xml":
        request_data = jsonToXml(request_data_dict)
        headers = {"Content-Type":"text/xml"}
    else:
        request_data = json.dumps(request_data_dict)
        headers = {"Content-Type": "application/json"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(2)
    res = type_to_json(res)
    response_dict = {
        "res":res,
        "message":genxin_message,
        "request_data":request_data_dict
    }
    return response_dict


def open_zhi_red_bill(api_file, api_name, message, changemessag, geshi=geshi_peizhi):
    """
        红票开票，先开蓝票，获取代码号码
    """
    changemessage = deepcopy(changemessag)
    if "dsqz" in api_name:
        changemessage["REQUEST_COMMON_FPKJ.XSF_MC"] = xs_mc
        changemessage["REQUEST_COMMON_FPKJ.XSF_NSRSBH"] = xs_sbh
        url = qianzhi_url
    else:
        url = pan_url
    message = get_message("", "", changemessage, messages=message)
    genxin_message = blue_to_red(message)
    if geshi == "xml":
        message = str(jsonToXml(genxin_message))
    else:
        message = dict_to_json(genxin_message)
    request_data_dict = get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1009")
    test_data = dict(Config(api_file).get(api_name))
    url = url
    method = test_data.get("method")
    if geshi=="xml":
        request_data = jsonToXml(request_data_dict)
        headers = {"Content-Type":"text/xml"}
    else:
        request_data = json.dumps(request_data_dict)
        headers = {"Content-Type": "application/json"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(2)
    res = type_to_json(res)
    response_dict = {
        "res":res,
        "message":genxin_message,
        "request_data":request_data_dict
    }
    return response_dict


def get_now_dmhm(api_file, api_name, message_file, messagename, fplx):
    """
        读取配置文件获取请求地址、请求参数，根据通用key将messages进行加密，并返回
    """
    message = Config(message_file).get(messagename)
    message = get_new_json(message, "REQUEST_COMMON_CXDQWKPH.KPZDBS", KPZDBS)
    message = get_new_json(message, "REQUEST_COMMON_CXDQWKPH.FPLXDM", fplx)
    message = get_new_json(message, "REQUEST_COMMON_CXDQWKPH.NSRSBH", xs_sbh)
    message = str(jsonToXml(message))
    request_data_dict = get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1010")
    test_data = dict(Config(api_file).get(api_name))
    url = qianzhi_url
    method = test_data.get("method")
    request_data = jsonToXml(request_data_dict)
    headers = {"Content-Type": "text/xml"}
    response = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(1)
    response = type_to_json(response)
    res = {"res": response}
    return res


def zuofei_fapiao(api_file, api_name, message):
    """
        读取配置文件获取请求地址、请求参数，根据通用key将messages进行加密，并返回
    """
    message = str(jsonToXml(message))
    request_data_dict = get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1012")
    test_data = dict(Config(api_file).get(api_name))
    url = qianzhi_url
    method = test_data.get("method")
    request_data = jsonToXml(request_data_dict)
    headers = {"Content-Type": "text/xml"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(1)
    res = type_to_json(res)
    return res


# 审批红字发票申请
def shenhe_hongzi(bludkj_res, ispass):
    response = type_to_json(decode_base64(jiexi_json(bludkj_res, "res.interface.Data.content")))
    fpdm = response["FP_DM"]
    fphm = response["FP_HM"]
    sqbh = get_zhuan_bianma_16()
    op_mysql = OperationMysql(db_peizhi)
    if ispass == "tongguo":
        sql = "update dj_hzxxb_sq set xxbbh=%d, clbz=2 where lzfpdm=%s and lzfphm=%s ;" %(int(sqbh), fpdm, fphm)
    if ispass == "dahui":
        sql = "update dj_hzxxb_sq set clbz=3,spbz='%s' where lzfpdm=%s and lzfphm=%s ;" % ("N", fpdm, fphm)
    if ispass == "butongguo":
        sql = "update dj_hzxxb_sq set clbz=3 where lzfpdm=%s and lzfphm=%s ;" % (fpdm, fphm)
    res = op_mysql.update(sql)
    return res


def zhuanshenqing_fapiao(api_file, api_name, message):
    """
        读取配置文件获取请求地址、请求参数，根据通用key将messages进行加密，并返回
    """
    message = str(jsonToXml(message))
    request_data_dict = get_request_data_message_json(api_file, api_name, message, intefacecode="DFXJ1011")
    test_data = dict(Config(api_file).get(api_name))
    url = qianzhi_url
    method = test_data.get("method")
    request_data = jsonToXml(request_data_dict)
    headers = {"Content-Type": "text/xml"}
    res = requests.request(method, url, headers=headers, data=request_data, verify=False).text
    time.sleep(1)
    res = type_to_json(res)
    return res


def search_bill(API_data_file, apiurl, search_message, dict_result, pan):
    """
    查询发票请求接口
    """
    if "dsqz" in apiurl:
        url = qianzhi_url
    else:
        url = pan_url
    open_message = dict_result["message"]
    open_request_data = dict_result["request_data"]

    test_data = dict(Config(API_data_file).get(apiurl))

    url = url
    method = test_data.get("method")
    father_dir = get_father_path(API_data_file)
    message = dict(Config(os.path.join(father_dir,"pan\open_bill_message.yml")).get(search_message))

    message = change_pan_search(message,pan)
    FPQQLSH = jiexi_json(open_message, "REQUEST_COMMON_FPKJ.FPQQLSH")
    message = get_new_json(message,"REQUEST_COMMON_FPCX.FPQQLSH", FPQQLSH)

    message = dict_to_json(message)
    message_base64 = encode_base64(message)
    message_base64 = message_base64.replace("\n", "")
    request_data = dict(open_request_data)
    request_data = get_new_json(request_data,"interface.Data.content",message_base64)

    contentkey = request_encryption(message, SECRET_KEY)
    request_data = get_new_json(request_data, "interface.Data.contentKey",contentkey)

    request_data = get_new_json(request_data, "interface.globalInfo.interfaceCode", "DFXJ1004")
    dataExchangeId = "DZFPQZDFXJ1001" + str(get_time_2())+str(get_random_FPQQLSH_9())
    request_data = get_new_json(request_data,"interface.globalInfo.dataExchangeId",dataExchangeId)

    request_data_json = json.dumps(request_data)
    res = requests.request(method, url, data=request_data_json).text
    time.sleep(2)
    res = response_into_json(res)
    return res


def blue_to_red(resquesedata):
    """
    将blue票报文修改成红票报文
    :param resquesedata:
    :return:
    """
    JSHJ = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.JSHJ"))
    HJJE = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.HJJE"))
    HJSE = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.HJSE"))
    resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.KPLX", "1")
    resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.JSHJ", JSHJ)
    resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.HJJE", HJJE)
    resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.HJSE", HJSE)
    mingxi_json = jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX")
    if isinstance(mingxi_json, dict):
        XMSL = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.XMSL"))
        XMJE = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.XMJE"))
        SE = "-" + str(jiexi_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.SE"))
        resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.XMSL", XMSL)
        resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.XMJE", XMJE)
        resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX.SE", SE)
    if isinstance(mingxi_json, list):
        mingxis = []
        for mingxi in list(mingxi_json):
            XMSL = dict(mingxi).get("XMSL")
            XMJE = dict(mingxi).get("XMJE")
            SE = dict(mingxi).get("SE")
            if XMSL != None:
                mingxi["XMSL"] = "-" + str(XMSL)
            mingxi["XMJE"] = "-" + str(XMJE)
            mingxi["SE"] = "-" + str(SE)
            mingxis.append(mingxi)
        resquesedata = get_new_json(resquesedata, "REQUEST_COMMON_FPKJ.COMMON_FPKJ_XMXXS.COMMON_FPKJ_XMXX", mingxis)
    return resquesedata


def while_search(API_data_file, api_name, search_message, blue_result, pan):
    response_search = None
    for i in range(12):
        time.sleep(3)
        response_search = search_bill(API_data_file, api_name, search_message, blue_result, pan)
        result_search = get_respont_result(response_search)
        if result_search.get("returnCode") == "0000":
            print_log("查询成功" + result_search.get("returnMessage"))
            break
        elif i > 10:
            print_log("查询超时" + result_search.get("returnMessage"))
            raise Exception("查询超时")
        elif result_search.get("returnCode") == "0001":
            continue
        else:
            print_log(result_search.get("returnCode")+"____"+result_search.get("returnMessage"))
            raise Exception("异常情况")
    return response_search


def get_respont_result(res):
    res = dict(res)
    returnMessage = jiexi_json(res,"interface.returnStateInfo.returnMessage")
    returnCode = jiexi_json(res, "interface.returnStateInfo.returnCode")
    dict_result = {
        "returnCode":returnCode,
        "returnMessage":returnMessage
    }
    return dict_result



















