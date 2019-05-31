#!/usr/bin/env python
# coding=utf-8
"""封装或取报文模板对象的方法"""
from Common.util.edit_file.edit_xml import *
from Common.util.get_dir import *
import os
xml_dir = os.path.join(get_how_dir(os.path.abspath(__file__), 3), "data", "xml_message")  # 模板存在文件夹路劲


def get_msg_tongyong():
    """获取通用报文模板对象"""
    msgfile = os.path.join(xml_dir, "tongyong.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_dp_kp():
    """获取电票开票模板对象"""
    msgfile = os.path.join(xml_dir, "dp_kaiju.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_dp_downurl():
    """获取电票pdf下载地址查询模板对象"""
    msgfile = os.path.join(xml_dir, "dp_downurl_search.xml")
    msg = read_xml(msgfile).toprettyxml()
    return msg


def get_msg_dp_jieyu_search():
    """获取电票结余查询模板对象"""
    msgfile = os.path.join(xml_dir, "dp_jieyu_search.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_dp_kuaisu_hongchong():
    """获取快速红冲模板对象"""
    msgfile = os.path.join(xml_dir, "dp_kuaisu_hongchong.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_dp_search():
    """获取电票查询模板对象"""
    msgfile = os.path.join(xml_dir, "dp_search.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_zp_dayin():
    """获取纸票打印模板对象"""
    msgfile = os.path.join(xml_dir, "zp_dayin.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_zp_hongzi():
    """获取纸票红字申请模板对象"""
    msgfile = os.path.join(xml_dir, "zp_hongzi_shenqinandsearch.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_zp_kaiju():
    """获取纸票开具模板对象"""
    msgfile = os.path.join(xml_dir, "zp_kaiju.xml")
    msg = read_xml(msgfile)
    return msg


def get_msg_zp_nextbill():
    """获取纸票未开票号模板对象"""
    msgfile = os.path.join(xml_dir, "zp_nextbill_search.xml")
    msg = read_xml(msgfile)


def get_msg_zp_zuofei():
    """获取纸票作废模板对象"""
    msgfile = os.path.join(xml_dir, "zp_zuofei.xml")
    msg = read_xml(msgfile)
    return msg





