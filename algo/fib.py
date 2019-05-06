# 斐波拉基
# 递归算法
# def fib_recur(n):
#     assert n >= 0, "n > 0"
#     if n <= 1:
#         return n
#     return fib_recur(n-1) + fib_recur(n-2)
# for i in range(1, 20):
#     print(fib_recur(i), end=' ')

# 生成器
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a+b
        max -= 1
        yield a
        for i in fib_loop_while(10):
            print(i)
