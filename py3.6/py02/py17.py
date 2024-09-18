# 元组, 元组只能创建，不可以修改
x = ('aa', 'bb' , 'cc')
a = x[0]
print(a)

# 利用+和*操作符，可以由现有元组创建新的元组
xx = x + x
print(xx)

x2 = x * 2
print(x2)

# 元组副本的创建方式，与列表完全相同
x_ = x[:]
print(x_)

x_ = x * 1
print(x_)

x_ = x + ()
print(x_)

# 单个元素的元组应加上逗号
v1 = 3
v2 = 4
v3 = (v1 + v2,)
print(v3)

# 元组的打包和拆包
(a, b, c, d) = (1, 2, 3, 4)
print(a, b, c, d)

a, b, c, d = 11, 12, 13, 14
print(a, b, c, d)

value = (1, 2, 3, 4, 5, 6)
a, b, *c = value
print(a, b, c)

a, *b, c = value
print(a, b, c)

*a, b, c = value
print(a, b, c)

# 列表和元组的相互转换
tp = (1, 2, 3, 4, 5, 6)
print(list(tp))

lt = [1, 2, 3, 4, 5, 6]
print(tuple(lt))

