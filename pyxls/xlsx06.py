#!/usr/bin/env python

import openpyxl

book = openpyxl.load_workbook('items.xlsx')

sheet = book.active

cells = sheet['A1': 'C14']
# 这里接收的变量需和遍历的列数一致
for c1, c2, c3 in cells:
    print("{0:8} {1:8} {2:8}".format(c1.value, c2.value, c3.value))

