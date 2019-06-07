# 集合的创建
# set 存储无序不可重复的元素
s = set('zha xin')
# print(s)

s1 = ['aa', 'bb', 'cc']
# 列表转集合
s2 = set(s1)
# print(s2, type(s2))

# 集合转列表
s3 = list(s2)
# print(s3, type(s3))

# 集合分为可变集合和非可变集合
# set frozenset
# print('aa' in s1)
# 将字符作为一个元素添加到集合
s2.add('uu')
# 将字符作为序列, 序列里的每个内容添加到集合中
s2.update('ops')
# print(s2)

# 删除指定元素
s4 = set(['12', '23', '34', '45'])
# s4.remove('12')
# print(s4)

# 随机删除某个元素
# s4.pop()
# print(s4)

# clear 清空元素
# s4.clear()
# print(s4)

# del 集合后该集合就不存在了
# del s4
# print(s4)

# 集合的等价和不等价 == !=
print(set('zha') == set('zzhxx'))

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
# intersection 交集
# print(a.intersection(b))
# print(a & b)

# union并集
# print(a.union(b))
# print(a | b)

# difference差集
# print(a.difference(b))
# print(a - b)

# symmetric_difference对称差集 / 反向交集
# print(a.symmetric_difference(b))
# print(a ^ b)

# 超集(a是否完全包含b)
# print(a.issuperset(b))
# print(a > b)

# 子集
# print(a.issubset(b))
# print(a < b)
