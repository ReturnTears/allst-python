import sys, time

# 隔4.4s才打印到控制台
# 先将数据存入到缓存区, 最后才将数据打印出来
# 加上flush就会立即刷新, 呈现出进度条的形式
for i in range(22):
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.2)

# w+, 对文件的写都是从文件的末尾开始, 这是存储机制决定的
f = open('../../static/file/wrtFile', 'w+', encoding='UTF8')
print(f.tell())
print(f.readline())
f.write('missing you away')
f.close()

