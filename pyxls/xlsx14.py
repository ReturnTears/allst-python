#!/usr/bin/env python

from openpyxl import Workbook
from openpyxl.styles import Alignment

book = Workbook()
sheet = book.active
# 冻结窗格时，在滚动到工作表的另一个区域时，我们会保持工作表的某个区域可见。
sheet.freeze_panes = 'B2'

book.save('freezing.xlsx')

