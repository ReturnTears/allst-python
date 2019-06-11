# Auther    Junn
# Date      2019-06-07
# Description 函数返回值
def funb():
    print('ok')
    return 'hello world'
# 获取返回值
str = funb()
print(str)

def foo():
    # return后面可以跟多个对象，这些对象被当作一个元组对象返回
    return 1, 'abc', 7

# 函数是默认返回None的
a = foo()
print(a)

# 高阶函数
# 函数本身也是一个变量, 函数名既可以作为函数参数，还可以作为函数的返回值
def fn(n):
    return n * n

print(fn(4))

def f(a, b, f):
    return f(a) + f(b)

res = f(1, 2, fn)
print(res)

def funct():
    def inner():
        return 7
    return inner
# ret是函数的inner的内存引用地址
ret = funct()
# print(ret)
print(ret())


