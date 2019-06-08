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
    # 局部作用域中声明某个变量是全局的
    global count
    print(count)    # 10
    # count = 5 这里会报错,但是去掉print函数就正确。因为局部不能修改全部变量，去掉print表示重新定义局部变量(这个解释不是很合理),
    #                                         因为在调用outer2函数时，局部的所有内容已经加载到了内存中，此时print函数打印的变量是局部的而不是全局的，由于变量声明在打印函数的下面，顺序执行的时候找不到该变量
    # count += 1 这里没有上面的两行语句依然报错，因为count = count + 1, 第一个count表示局部变量，第二个count表示全局变量，局部不能修改全部变量
    # 想要修改的话，需要用到global关键字声明一下
    count += 1
    print(count)    # 11
outer2()

'''
小结:
    1、变量的查找顺序: LEGB
    2、只有模块、类、以及函数才能引入新作用域
    3、对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用就会使用外部作用域的变量
    4、内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字，(nonlocal是python3新增，有了它可以完美实现闭包)
    
'''




