# Auther    Junn
# Date      2019-06-07
# Description 作用域:
# local:局部作用域，在函数中定义的变量
# enclosing:嵌套的父级函数的局部作用域，包含在此函数的上级函数的局部作用域，但不是全局的
# global: 全局变量，模块级别定义的变量
# built-in: 系统固定模块里面的变量
# 搜索变量的优先级依次是: 作用域局部 > 外层作用域 > 当前模块中的全局 > python内置的作用域 LEGB

a = int(6.22)           # built-in
b = 0                   # global
def outer():
    c = 1               # enclosing
    def inner():
        d = 2           # local
        print(c)
    inner()
    # print(d)      找不到变量d
# outer()

# 变量的修改
count = 10
def outer2():
    # print函数的
    print(count)
    # count = 5 这里会报错,但是去掉print函数就正确。因为局部不能修改全部变量，去掉print表示重新定义局部变量
    # count += 1 这里没有上面的两行语句依然报错，因为count = count + 1, 第一个count表示局部变量，第二个count表示全局变量，局部不能修改全部变量






