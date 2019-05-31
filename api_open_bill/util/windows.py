#!/usr/bin/env python
# coding=utf-8


import os
import pyperclip


# 删除文件
def rm_file(file):
    os.remove(file)


# 执行命令shell
def run_shell(shell):
    os.system(shell)


# 判断目标文件是否存在
def file_is_exists(file):
    return os.path.exists(file)


# 获取目标文件的路径和文件名
def get_dir_file(file):
    dir_file_list = os.path.split(file)
    return dir_file_list


# 分开文件名和拓展名
def get_file_houzhui(file):
    file_houzhui_list = os.path.splitext(file)
    return file_houzhui_list


# 文件或文件夹的最后修改时间
def file_updata_time(file):
    updata_time = os.path.getmtime(file)
    return updata_time


# 文件或文件夹的创建时间
def file_creat_time(file):
    creat_time = os.path.getctime(file)
    return creat_time



# mknod创建空文件
def creat_Null_file(file):
    os.mknod(file)


# open直接打开一个文件，如果文件不存在则创建文件
def open_creat_file(file):
    open(file,"w")


# 创建目录
def creat_dir(path):
    os.mkdir(path)


# 创建多级目录
def creat_dirs(path):
    os.makedirs(path)


# 复制
def copy(text):
    pyperclip.copy(text)


# 粘贴
def paste():
    text = pyperclip.paste()
    return text


# 判断str是否在文本中
def str_isin_file(str1,file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    flag = False
    for line in lines:
        flag = str1 in str(line)
        if flag :
            break
        else:
            continue
    return flag

#鼠标右键



