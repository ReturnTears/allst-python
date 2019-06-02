import sys, time

# 隔4.4s才打印到控制台
# 先将数据存入到缓存区, 最后才将数据打印出来
# 加上flush就会立即刷新, 呈现出进度条的形式
# for i in range(22):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.2)

# Method2
# for l in range(30):
#     print('*', end='', flush=True)
#     time.sleep(0.1)

# truncate() 截断数据(不能再r模式下)
# 在w模式下：先清空，再写，再截断
# 在a模式下：直接将指定位置后的内容截断
# file = open('../../static/file/wrtFile', 'w', encoding='UTF8')
# file.truncate(5)
# file.write('Hello World !')
# file.truncate(5)
# file.close()

# r+:光标默认在0位置，最后位置开始写
# w+:先清空，再写读
# a+:光标默认在最后位置

# w+, 对文件的写都是从文件的末尾开始, 这是存储机制决定的
# f = open('../../static/file/wrtFile', 'w+', encoding='UTF8')
# print(f.tell())
# print(f.readline())
# f.write('missing you away')
# f.close()

# 如何在磁盘修改文件: 采取重新创建一个文件的思路
# fileRead = open('../../static/disk/readFile.txt', 'r', encoding='UTF8')
# fileWrite = open('../../static/disk/writeFile.txt', 'w', encoding='UTF8')
# number = 0
# for num in fileRead:
#     number += 1
#     if number == 5:
#         num = ''.join([num.strip(), 'XiAoHu\n'])
#     fileWrite.write(num)
#
# fileRead.close()
# fileWrite.close()

# with 推荐使用， 可以同时管理多个文件对象
with open('../../static/disk/readFile.txt', 'r', encoding='UTF8') as fread,\
        open('../../static/disk/writeFile.txt', 'w', encoding='UTF8') as fwrite:
    for line in fread:
        fwrite.write(line)



