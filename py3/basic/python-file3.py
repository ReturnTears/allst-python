# 想在文件的第4行后面添加点内容
file = open('../../static/file/demoFile', 'r', encoding='utf8')
data = file.readlines() # 文件较大时不要使用readlines
file.close() #只对一个文件操作，可以读取到文件后就将其关闭
num = 0
for i in data:
	num += 1
	if num == 4:
		i = ''.join([i.strip(), '********']) # 字符串的拼接用join不用+

f = open('../../static/file/demoFile', 'r', encoding='UTF-8')
for j in f:      # 这里是for内部将f对象处理成了一个迭代器, 读一行取一行
    print(j.strip())

# 获取光标的位置   tell会区分中英文, 英文1个字符, 中文3个字符
print(f.tell())
# 调整光标的位置   --场景:(上传文件时可以实现断点续传)
f.seek(0)
