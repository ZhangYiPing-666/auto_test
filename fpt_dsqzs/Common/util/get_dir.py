#!/usr/bin/env python
# coding=utf-8
import os


def get_how_dir(file_dir, num):
    """根据传入的数字获取多少层级的父目录"""
    for i in range(num):
        file_dir = os.path.dirname(file_dir)
    return file_dir


def join_dir(arg, *args):
    if len(args) == 0:
        file_dir = arg
    else:
        for i in args:
            file_dir = os.path.join(arg,i)
            arg = file_dir
    return file_dir





