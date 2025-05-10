#!/usr/bin/env python

import openpyxl

# 每个工作簿可以有多个工作表

book = openpyxl.load_workbook('sheets.xlsx')
# get_sheet_names 函数过时了
print(book.sheetnames)

active_sheet = book.active
print(type(active_sheet))
# get_sheet_by_name 函数过时了
sheet = book["Phone"]
print(sheet.title)

