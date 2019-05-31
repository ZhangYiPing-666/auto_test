#!/usr/bin/env python
# coding=utf-8


import json
import xmltodict


# 读取json文件
def read_data(self):
	with open(self.file_path,'r') as fp:
		data = json.load(fp)
		return data


# 根据关键字获取数据
def get_data(self,id):
	print (type(self.data))
	return self.data[id]


# 写json
def write_data(self,data):
	with open('../dataconfig/cookie.json','w') as fp:
		fp.write(json.dumps(data))


# 修改json中某个key的值
def get_new_json(json_data, key, value):
	key_ = key.split(".")
	key_length = len(key_)
	i = 0
	json_data = dict(json_data)
	a = json_data
	while i < key_length:
		if i + 1 == key_length:
			a[key_[i]] = value
			i = i + 1
		else:
			a = a[key_[i]]
			i = i + 1
	return json_data


# 修改json中某个key的值
def inster_new_json(json_data, key, value):
	key_ = key.split(".")
	key_length = len(key_)
	i = 0
	json_data = dict(json_data)
	a = json_data
	while i < key_length:
		if i + 1 == key_length:
			a[key_[i]] = value
			i = i + 1
		else:
			a = a[key_[i]]
			i = i + 1
	return json_data


# 解析返回的json获得关键key值
def jiexi_json(json_data, key):
	a = key.split(".")
	value = json_data
	for i in a:
		value = value[i]
	return value


# 将json格式转换为xml
def jsonToXml(js):
	convertXml = ''
	jsDict = js
	try:
		convertXml = xmltodict.unparse(jsDict, encoding='utf-8')
	except:
		convertXml = xmltodict.unparse({'request': jsDict}, encoding='utf-8')
	finally:
		return convertXml


# 校验json里面是否有对应的key
def key_excit_json(json_1, key):
	json_1 = json.dumps(json_1)
	keylsit = key.split(".")
	if keylsit[-1] in json_1:
		return True
	else:
		return False


# 将数据格式转换为json
def type_to_json(response):
	if response[0] == "{":  # 字符串转换json
		response = json.loads(response)
	elif response[0] == "<":  # xml转换json
		xml = xmltodict.parse(response)
		response = json.dumps(xml, indent=1)
		response = json.loads(response)
		if key_excit_json(response, "RESPONSE"):
			response = response["RESPONSE"]
	else:
		raise Exception("传入的数据不能转换json格式")
	return response


# 将dict格式转换成jsonstr
def dict_to_json(dict_name):
	jsonstr = json.dumps(dict_name, ensure_ascii=False)
	return jsonstr

