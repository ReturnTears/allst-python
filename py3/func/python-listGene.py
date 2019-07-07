# Auther    Junn
# Date      2019-07-07
# Description 列表生成式

'''
    第一步从for x in range(10)当作整体取值
    第二步前面的表达式引用后面的值, 前面的表达式可以是变量，表达式，函数
'''
def func(n):
    return n**3
a = [func(x) for x in range(10)]
print(a)
print(type(a))

"""
补充:
    类似赋值，b=t[0],c=t[1]
"""
t=['xiaohu', 7]
b,c = t
print(b)
print(c)