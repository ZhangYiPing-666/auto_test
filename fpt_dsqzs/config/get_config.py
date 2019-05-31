#!/usr/bin/env python
# coding=utf-8
"""封装方法获取配置文件config.ini的值"""

import os
import codecs
import configparser
from Common.util.get_dir import *

file = os.path.abspath(__file__)
config_dir = os.path.join(get_how_dir(file, 1), "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(config_dir)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(config_dir, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(config_dir)

    def get_email(self):
        value = dict(self.cf.items("EMAIL"))
        return value

    def get_http(self):
        value = dict(self.cf.items("HTTP"))
        return value

    def get_db(self):
        value = dict(self.cf.items("DATABASE"))
        return value



