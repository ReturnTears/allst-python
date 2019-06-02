# file operation（打开、操作、关闭）
# 三种基本的操作模式: r只读 w只写 a追加
# open方法获取文件对象
file = open('../../static/file/demoFile', 'r', encoding='UTF-8')
# read()读取文件所有的内容 read(num) 读取内容字符:英文一个字母一个字符，中文一个字资格字符
readData = file.read(10)    # 汉字在这里占一个单位(in python3)
print(readData)
print(file.readline())      # 无论是read()还是readline(),光标会发生位置变化
print(file.readlines())     # 会打印带\n的字符串
# 报错 读写要区分，
# writeData = file.write('Hello Python')

# 关闭文件
file.close()
# ------------------------------------------------------------------------------
# 同一个文件读写操作时写操作会覆盖掉之前的内容，若文件不存在就创建文件
wrt = writeFile = open('../../static/file/wrtFile', 'w', encoding='UTF-8')
wrt.write('Hello Python \n')
# 写操作不会就是在内容后面追加
wrt.write('Hello YangYang')

wrt.close()
# -------------------------------------------------------------------------------
# 实例1
f = open('../../static/file/demoFile', 'r', encoding='UTF-8')
data = f.readlines()
num = 0
for line in data:
    num += 1
    if num == 7:
        line = ''.join([line.strip(), '************'])      # 取代万恶的+
        print(line.strip())
f.close()

# 实例2
# 对于大数据文件, 要用一下方式
f2 = open('../../static/file/demoFile', 'r', encoding='UTF-8')
num2 = 0
for i in f2:
    num2 += 1
    if num2 == 7:
        i = ''.join([i.strip(), '#######'])
    print(i.strip())

print(f2.tell())    # 取出光标位置
f2.seek(7)          # 移动光标到指定位置
f2.flush()          # 将数据从缓存转移到磁盘上去 --> python-file2.py
