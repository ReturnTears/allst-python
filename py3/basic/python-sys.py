# author        JUNN
# since         2019-08-20 下午 11:29
# description   sys模块-和python解析器交互

import sys
# 命令行参数List, 第一个元素是程序本身路径
# 在命令行执行: python python-sys.py post path -> ['python-sys.py', 'post', 'path']
print(sys.argv)
def post():
    print('ok')
def down():
    pass
if sys.argv[1] == 'post':
    post()
elif sys.argv[1] == 'down':
    down()

# 程序退出,正常退出时sys.exit(0)
# sys.exit(0)

# 获取python解释程序的版本信息
print(sys.version)

# 最大的Int值
print(sys.maxsize)

# 返回模块的额搜索路径,初始化时使用python path环境变量的值
print(sys.path)

# 返回操作系统平台名称, 可以通过它写出跨平台的程序
print(sys.platform)

#
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]