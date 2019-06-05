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
print(s)


