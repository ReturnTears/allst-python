import openpyxl

def write_to_excel(path, sheet_name, data):
# 创建一个新的工作簿
    workbook = openpyxl.Workbook()
# 激活一个工作表
    sheet = workbook.active
# 设置工作表名称
    sheet.title = sheet_name

# 遍历数据并写入到工作表
    for row_index, row_data in enumerate(data):
        for col_index, value in enumerate(row_data):
            sheet.cell(row=row_index + 1, column=col_index + 1, value=value)

# 保存工作簿
    workbook.save(path)
    print('写入成功')

# 示例数据
data = [['Name', 'Age', 'City'], ['John Doe', 28, 'New York'], ['Jane Smith', 34, 'Los Angeles']]
write_to_excel('example.xlsx', 'Sheet1', data)
