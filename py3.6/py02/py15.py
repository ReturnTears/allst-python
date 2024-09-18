# 用in操作符判断列表成员
first = [1,2,3,4,5]
res = 3 in first
print(res)

res = 3 not in first
print(res)

# 用+操作符拼接列表
second = [6,7,8,9]
third = first + second
print(third)

# 用*操作符初始化列表
four = [None] * 5
print(four)

five = [1, 2, 3] * 2
print(five)

# 用min和max方法求列表的最小值和最大值

six = [3, 6, 9, 1, 2, 5, 8, 4, 7]
print(min(six))
print(max(six))

# 用index方法搜索列表
idx = six.index(8)
print(idx)

# 用count方法对匹配项计数
seven = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print(seven.count(2))

# 用sort方法对列表排序
seven.sort()
print(seven)

# len方法
print(len(seven))
