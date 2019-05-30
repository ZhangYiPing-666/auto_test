#!/usr/bin/env python
# coding=utf-8

"""
文件读取。YamlReader读取yaml文件
"""


import yaml
import os


class YamlReader(object):
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data


class Config:
    def __init__(self, file):
        self.config = YamlReader(file).data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)
