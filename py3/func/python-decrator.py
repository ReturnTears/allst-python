# Auther    Junn
# Date      2019-06-19
# 装饰器也是特殊的函数
import time

def show(f):
    # 添加装饰器
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('spend %s' %(end - start))
    return inner

def show2(f):
    # 添加装饰器
    def inner(a, b):
        start = time.time()
        f(a, b)
        end = time.time()
        print('spend %s' %(end - start))
    return inner

def show3(f):
    # 添加装饰器
    def inner(*a, **b):
        start = time.time()
        f(*a, **b)
        end = time.time()
        print('spend %s' %(end - start))
    return inner

# 给装饰器添加参数
def logger(flag = ''):
    def show4(f):
        # 添加装饰器
        def inner(a, b):
            start = time.time()
            f(a, b)
            end = time.time()
            print('spend %s' %(end - start))
            if flag == 'true':
                print('日志记录.')
        return inner
    return show4

@show # 等价于 foo = show(bar)
def foo():
    print('come in foo...')
    time.sleep(2)
@show
def bar():
    print('come in bar...')
    time.sleep(3)

# foo()  # 执行inner函数

# 功能函数加参数
@show2
def add(a, b):
    print(a + b)
    time.sleep(1)
# add(1, 2)

@show3
def addNums(*a, **b):
    sums = 0
    for i in a:
        sums += i
    print(sums)
    time.sleep(1)

# addNums(1, 2, 3, 5, 6, 7)

@logger('true')
def adds(a, b):
    print(a + b)
    time.sleep(2)

adds(1, 6)

