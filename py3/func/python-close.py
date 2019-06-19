# Auther    Junn
# Date      2019-06-19
# 函数的闭包:如果在一个内部函数里,对在外部作用域(但不是在全局作用域)的变量进行引用，那么内部函数就被任务是闭包(closure)
# 闭包 = 内部函数 + 定义函数时的环境
def outer():
    x = 7
    def inner():
        print(x)
    return inner
# 调用inner
# outer()()

# 直接调用inner报错, 局部变量，全局无法调用
# inner()

func = outer()
func()
