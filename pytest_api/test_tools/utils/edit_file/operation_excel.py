#!/usr/bin/env python
# coding=utf-8

"""
Created on 2019年07月20日
@author: zhangyp
describe：开票测试用例
"""


import os
import xlrd
from xlutils.copy import copy
from xlrd import open_workbook


class OperationExcel(object):
	def __init__(self,file_name=None,sheet=None):
		if file_name:
			self.file_name = file_name
			self.sheet = sheet
		else:
			self.file_name = '../dataconfig/case1.xls'
			self.sheet = 0
		self.data = self.get_data()

	def get_data(self): 	# 获取sheets的内容
		data = xlrd.open_workbook(self.file_name)
		if type(self.sheet) == int:
			table = data.sheet_by_index(self.sheet)
		else:
			table = data.sheet_by_name(self.sheet)
		return table

	# 获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	# 获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	# 写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)

	# 根据对应的caseid 找到对应行的内容
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	# 根据对应的caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		clols_data = self.get_cols_data()
		for col_data in clols_data:
			if case_id in col_data:
				return num
			num = num+1

	# 根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)
		return row_data

	# 获取某一列的内容
	def get_cols_data(self, col_id=None):
		if col_id != None:
			cols = self.data.col_values(col_id)
		else:
			cols = self.data.col_values(0)
		return cols


class SheetTypeError(Exception):
	pass


class ExcelReader_Row_Litle:
	"""
	读取excel文件中的内容。返回list。
	行为title
	如：
	excel中内容为：
	| A  | B  | C  |
	| A1 | B1 | C1 |
	| A2 | B2 | C2 |

	如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
	[{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

	如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
	[[A,B,C], [A1,B1,C1], [A2,B2,C2]]

	可以指定sheet，通过index或者name：
	ExcelReader(excel, sheet=2)
	ExcelReader(excel, sheet='BaiDuTest')
	"""
	def __init__(self, excel, sheet=0, title_line=True):
		if os.path.exists(excel):
			self.excel = excel
		else:
			raise FileNotFoundError('文件不存在！')
		self.sheet = sheet
		self.title_line = title_line
		self._data = []

	def data(self):
		if not self._data:
			workbook = open_workbook(self.excel)
			if type(self.sheet) not in [int, str]:
				raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
			elif type(self.sheet) == int:
				s = workbook.sheet_by_index(self.sheet)
			else:
				s = workbook.sheet_by_name(self.sheet)

			if self.title_line:
				title = s.row_values(0)  # 首行为title
				for col in range(1, s.nrows):
					# 依次遍历其余行，与首行组成dict，拼到self._data中
					self._data.append(dict(zip(title, s.row_values(col))))
			else:
				for col in range(0, s.nrows):
					# 遍历所有行，拼到self._data中
					self._data.append(s.row_values(col))
		return self._data


class ExcelReader_Clo_Litle:
	"""
	读取excel文件中的内容。返回list。
	列为title
	如：
	excel中内容为：
	| A | A1 | A2 |
	| B | B1 | B2 |
	| C | C1 | C2 |

	如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
	[{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

	如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
	[[A,B,C], [A1,B1,C1], [A2,B2,C2]]

	可以指定sheet，通过index或者name：
	ExcelReader(excel, sheet=2)
	ExcelReader(excel, sheet='BaiDuTest')
	"""

	def __init__(self, excel, sheet=0, title_line=True):
		if os.path.exists(excel):
			self.excel = excel
		else:
			raise FileNotFoundError('文件不存在！')
		self.sheet = sheet
		self.title_line = title_line
		self._data = []

	def data(self):
		if not self._data:
			workbook = open_workbook(self.excel)
			if type(self.sheet) not in [int, str]:
				raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
			elif type(self.sheet) == int:
				s = workbook.sheet_by_index(self.sheet)
			else:
				s = workbook.sheet_by_name(self.sheet)

			if self.title_line:
				title = s.col_values(0)  # 首列为title
				for row in range(1, s.ncols):
					# 依次遍历其余行，与首行组成dict，拼到self._data中
					self._data.append(dict(zip(title, s.col_values(row))))
			else:
				for col in range(0, s.ncols):
					# 遍历所有行，拼到self._data中
					self._data.append(s.col_values(col))
		return self._data
