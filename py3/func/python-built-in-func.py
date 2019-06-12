# Auther    Junn
# Date      2019-06-12
# Description Python内置函数
# 内置函数是python自定义好的函数

# 绝对值
a = abs(-22)
# 元素有空返回False
b = all([1,2,'','all'])
# eval
c = eval('1+2*3-4')
# filter
d = ['a','b','c','d']
def fun1(s):
    if s != 'a':
        return s
ret = filter(fun1, d)
# map
def fun2(s):
    return s + "hello"
ret2 = map(fun2, d)
print(list(ret2))
# reduce
from functools import reduce
def add1(x, y):
    return x + y
# range函数含首不含尾
print(reduce(add1, range(1, 5)))

# lambda表达式
# 阶乘
f = reduce(lambda x,y:x*y, range(1,5))
print(f)