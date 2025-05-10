#!/usr/bin/env python

from openpyxl import Workbook

book = Workbook()
sheet = book.active

rows = (
    (34, 26),
    (88, 36),
    (24, 29),
    (15, 22),
    (56, 13),
    (76, 18)
)

for row in rows:
    sheet.append(row)

# openpyxl不进行计算； 它将公式写入单元格。
cell = sheet.cell(row=7, column=2)
cell.value = "=SUM(A1:B6)"
# cell.font = cell.font.copy(bold=True)
cell.font = cell.font.copy(bold=True)

book.save('formulas.xlsx')

