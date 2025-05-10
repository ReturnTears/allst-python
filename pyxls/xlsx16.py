#!/usr/bin/env python

from openpyxl import Workbook
from openpyxl.drawing.image import Image

book = Workbook()
sheet = book.active
# OpenPyXL 图像
img = Image("icon.png")
sheet['A1'] = 'This is Sid'

sheet.add_image(img, 'B2')

book.save("sheet_image.xlsx")

