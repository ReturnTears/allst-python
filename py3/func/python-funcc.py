# Auther    Junn
# Date      2019-06-11

'''
    递归函数:
        关于递归，在函数的内部需要调用自身函数， 有一个结束条件，但凡是递归可以实现的，循环都可以实现，递归的效率有时候是很低的
    内置函数
'''
# 循环实现阶乘
def fn(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

a = fn(5)
print(a)

# 递归实现阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

b = fact(5)
print(b)

# 递归实现斐波那契数列
# 1 1 2 3 5 8 13 21 34 55 ...
# f(2) = f(1) + f(0)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)
c = fibo(7)
print(c)

