#!/usr/bin/env python
# coding=utf-8
from util.operation_json import *


def get_respont_result(res):
    res = dict(res)
    returnMessage = jiexi_json(res,"interface.returnStateInfo.returnMessage")
    returnCode = jiexi_json(res, "interface.returnStateInfo.returnCode")
    dict_result = {
        "returnCode":returnCode,
        "returnMessage":returnMessage
    }
    return dict_result
