# if elif else
x = 10
if x > 0:
    print('x > 0')

y = -10
if y > 0:
    print('y > 0')
elif y < 0:
    print('y < 0')
else:
    print('y = 0')

# > < == != >= <=
print(x == y)
print(x != y)
print(x > y)


# and or not
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# python中，在布尔上下文中，0，空字符串，空列表，空字典，空元组，None，False都为假，否则为真
my_list = [1,2,3]
if my_list:
    print('list is not empty')

a = 10
b = 20
if a > 0 and b > 0:
    print('a and b are positive')
elif a < 0 or b < 0:
    print('a or b is negative')
else:
    print('a and b are zero')
