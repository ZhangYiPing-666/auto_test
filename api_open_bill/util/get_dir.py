#!/usr/bin/env python
# coding=utf-8


import os


def get_pwd():
    pwd = os.getcwd()
    return pwd


def get_father_path(file_dir):
    father_path = os.path.abspath(os.path.dirname(file_dir)+os.path.sep+".")
    return father_path


def get_grader_father_path(file_dir):
    grader_father = os.path.abspath(os.path.dirname(file_dir)+os.path.sep+"..")
    return grader_father


def join_dir(arg, *args):
    if len(args) == 0:
        file_dir = arg
    else:
        for i in args:
            file_dir = os.path.join(arg,i)
            arg = file_dir
    return file_dir





