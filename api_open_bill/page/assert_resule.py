#!/usr/bin/env python
# coding=utf-8
from page.get_respont import *
from page.print_log import *
from page.message_eidt import *

def arrequt_respont_openbill(res, returnCode):
    result = get_respont_result(res["res"])
    if result.get("returnCode") == returnCode:
        print_log(result.get("returnMessage"))
        print_log("测试通过")
    else:
        e = result.get("returnCode") + result.get("returnMessage")
        raise Exception(e)
    if returnCode == "0000":
        bill_message = get_debase64_bill_message(res["res"])
        print_number(bill_message)


def arrequt_respont_getdh(res, returnCode):
    result = get_respont_result(res)
    if result.get("returnCode") == returnCode:
        print_log(result.get("returnMessage"))
        print_log("测试通过")
    else:
        e = result.get("returnCode") + result.get("returnMessage")
        raise Exception(e)
    if returnCode == "0000":
        bill_message = get_debase64_bill_message(res)
        print_dm_hm(bill_message)


def arrequt_respont_zuofgei(res, returnCode):
    result = get_respont_result(res)
    if result.get("returnCode") == returnCode:
        print_log(result.get("returnMessage"))
        print_log("测试通过")
    else:
        e = result.get("returnCode") + result.get("returnMessage")
        raise Exception(e)
    if returnCode == "0000":
        bill_message = get_debase64_bill_message(res)
        print_zuofei(bill_message)


def arrequt_respont_pan_openbill(res, returnCode):
    result = get_respont_result(res["res"])
    if result.get("returnCode") == returnCode:
        print_log(result.get("returnMessage"))
        print_log("测试通过")
    else:
        e = result.get("returnCode") + result.get("returnMessage")
        raise Exception(e)


# 校验两个值相等
def assert_equare(qiwang,shiji):
    if qiwang == shiji:
        pass
    else:
        raise_str = "期望结果与实际结果不一致，期望结果为%s，实际结果为%s"%(qiwang,shiji)
        raise Exception(raise_str)


# 校验两个值相等
def assert_in(qiwang,shiji):
    if qiwang in shiji:
        pass
    else:
        raise_str = "期望结果不在实际结果中，期望结果为%s，实际结果为%s"%(qiwang,shiji)
        raise Exception(raise_str)




