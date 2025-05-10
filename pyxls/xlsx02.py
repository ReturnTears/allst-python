#!/usr/bin/env python

from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 1
# 写入单元格 B2
sheet.cell(row=2, column=2).value = 2

book.save('write2cell.xlsx')

