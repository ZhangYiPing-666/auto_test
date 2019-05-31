#!/usr/bin/env python
# coding=utf-8

import time


def print_log(text):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now_time+"  "+"--->"+"  "+text)


def print_number(response):
    print_log("\n")
    print_log("FPQQLSH-流水号" + "-->  " + response["FPQQLSH"])
    print_log("FP_DM-代码    " + "-->  " + response["FP_DM"])
    print_log("FP_HM-号码    " + "-->  " + response["FP_HM"])
    if "PDF_URL" in response.keys():
        print_log("url-:    " + "-->  " + response["PDF_URL"])


def print_dm_hm(response):
    print_log("\n")
    print_log("FP_DM-代码    " + "-->  " + response["DQFPDM"])
    print_log("FP_HM-号码    " + "-->  " + response["DQFPHM"])


def print_zuofei(response):
    print_log("\n")
    if response["FPQQLSH"] is not None:
        print_log("FPQQLSH-流水号    " + "-->  " + response["FPQQLSH"])
    print_log("FP_DM-代码    " + "-->  " + response["FP_DM"])
    print_log("FP_HM-号码    " + "-->  " + response["FP_HM"])
    print_log("ZF_RQ-作废日期    " + "-->  " + response["ZFRQ"])