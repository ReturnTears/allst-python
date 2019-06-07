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