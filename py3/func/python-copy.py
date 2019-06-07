# 拷贝:浅拷贝、深拷贝
# s = [1, 'zha', 'xin']
# s1 = [1, 'zha', 'xin']
# s1[0] = 2
# print(s)
# print(s1)

# s = [1, 'zha', 'xin']
# s2 = s.copy()
# print(s2)
# s2[0] = 2
# print(s2)
# print(s)

# 浅拷贝: 拷贝的是引用的内存地址
s = [[1, 2, 3], 'zha', 'xin']
s2 = s.copy()
print(s2)
s2[0][1] = 20
print(s2)
# s里面的内容也被修改了, 修改字符串时拷贝的没有变化, 修改列表时有变化
print(s)

# 深拷贝: 拷贝的整个对象
import copy
a = ["zha", 123, [10000, 5000]]
b = copy.deepcopy(a)
b[0] = "xin"
b[1] = 456

print(a, b)

