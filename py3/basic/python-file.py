# file operation（打开、操作、关闭）
# open方法获取文件对象
file = open('../../static/file/demoFile', 'r', encoding='UTF-8')
# read()读取文件所有的内容 read(num) 读取内容字符:英文一个字母一个字符，中文一个字资格字符
readData = file.read()
print(readData)
# 报错 读写要区分，
# writeData = file.write('Hello Python')

# 关闭文件
file.close()

# 同一个文件读写操作时写操作会覆盖掉之前的内容，若文件不存在就创建文件
wrt = writeFile = open('../../static/file/wrtFile', 'w', encoding='UTF-8')
wrt.write('Hello Python \n')
# 写操作不会就是在内容后面追加
wrt.write('Hello YangYang')

wrt.close()

