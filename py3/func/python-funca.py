# Auther    Junn
# Date      2019-06-07
# Description 函数的作用: 减少重复代码、可扩展性、保持代码的一致性
'''
函数的定义:
    def关键字, 函数名称最好见名知其意, 调用时直接写函数名+()
'''
def showFunc():
    print('ok')

# showFunc()

# 带参数的函数(关键字参数、必须参数)
def add(x, y):
    print(x + y)

# add(10, 12)

import time
# 日志记录函数
def logger(n):
    time_format = '%Y-%m-%d %X'
    # strftime获取当前时间
    time_current = time.strftime(time_format)
    with open('../../static/file/log.txt', 'a') as f:
        f.write('%s end action %s\n' %(time_current, n))

# action 函数
def action(n):
    print("start action method...")
    logger(n)

# action(1)

# 默认参数
def printInfo(name, age, gender='f'):
    if gender=='f':
        print('%s`s age is %d years old`s 男孩.'%(name, age))
    else:
        print('%s`s age is %d years old`s 女孩.'%(name, age))

# printInfo("xiao", 18)

# 不定长参数, args传递的参数无命名的参数
def adds(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

# adds(1,2,3,4)

# kw不定长参数
# args在左边, kwargs在右边这是固定的格式
def dumArgs(*args, **kwargs):
    # print(args)
    # print(kwargs)
    for i in kwargs:
        print('%s:%s'%(i, kwargs[i]))

dumArgs('abc', 18, 'f', job='it', hobby='girls', addr='cq')


