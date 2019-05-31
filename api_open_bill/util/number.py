#!/usr/bin/env python
# coding=utf-8

import time
import random


def get_time_3():
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return now_time


# 获取随机的16位数字
def get_random_FPQQLSH_16():
    FPQQLSH = random.randint(9,99)
    str_1 = str(get_time_3())+str(FPQQLSH)
    return str_1


def get_random_FPQQLSH_9():
    FPQQLSH = random.randint(99999999,999999999)
    str_1 = str(FPQQLSH)
    return str_1


def get_random_23():
    str_1 = random.randint(9999999999999999999999,99999999999999999999999)
    str_1 = str(str_1)
    return str_1


def get_random_19():
    str_1 = random.randint(999999999999999999,9999999999999999999)
    str_1 = str(str_1)
    return str_1


# 获取红字申请编码16位
def get_zhuan_bianma_16():
    suiji = str(random.randint(99999999999999,999999999999999))
    list_a = list(map(int, suiji))
    sub_naumer = 0
    for i in range(len(list_a)):
        sub_naumer = sub_naumer + list_a[i]
    yu_number = sub_naumer % 10
    suiji = suiji + str(yu_number)
    return suiji


# 格式化获取当前时间
def get_time():
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return now_time


# 格式化获取当前时间
def get_time_2():
    now_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
    return now_time
