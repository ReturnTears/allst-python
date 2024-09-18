# 集合
x = set([1,2,3,4,5,4,3,2,1])
print(x)

x.add(6)
print(x)

print(1 in x)

# | 并集
y = set([1, 5, 6, 7])
print(x | y)

# & 交集
print(x & y)

# ^ 差集
print(x ^ y)

z = frozenset(x)
print(z)

y = set([1, 2, 3, 5])
res = y.add(z)
print(res)
