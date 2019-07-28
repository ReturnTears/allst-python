# Auther    Junn
# Date      2019-07-07
# Descript  生成器
"""
生成器有两种生成方式:
    1、(x for x in range(n))
    2、yield关键字

<generator object <genexpr> at 0x007AFA20>
通过该方式获取的仅仅是对象, 需要数据的时候才生成
"""
a = (x * 2 for x in range(10))
print(a)
"""
通过内置函数获取第一个值,a.__next__()与next(a)两种方式等价
next(a)是依次取值，超出取值范围了会报错trace back
"""
print(a.__next__())
print(next(a))

# 生成器是可迭代对象
for i in a:
    print(i)

"""
    yield关键字生成生成器对象
    生成器也是函数，它与普通函数的不同点在于，调用函数时普通函数会执行，生成器不会执行
    区分它们，生成器函数有yield关键字
"""


def foo():
    print('generate')
    yield 1
    print('ok')
    yield 2


g = foo()
print(g)
# next(g)
# next(g)

"""
什么是可迭代对象:有iter方法的可执行的对象
举例斐波拉契数列: 0, 1, 2, 3, 5, 8, ...
"""


def fib(max):
    n, before, after = 0, 0, 1
    while n < max:
        print(after)
        before, after = after, before + after
        n += 1


fib(7)
