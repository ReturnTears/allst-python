# String
a = "Let's let`s go"
# 乘法表示重复输出
print(a * 2)
# 打印索引第二个位置到最后
print('HelloWorld'[2:])
# 判断源字符串是否包含子字符串
print('el' in 'Hello')
# 格式化字符串%
print('%s is a good girl' % 'Yangy')
# 字符串拼接 + / join 可以连接列表
b = ' let you go!'
c = ''.join([a, b])
print(c)

s = "Hello\tYangYang {age} and {addr}"
print(s.count('Y'))
print(s.capitalize())
print(s.center(22, '💗'))
print(s.endswith('ng'))
print(s.startswith('He'))
print(s.expandtabs(tabsize=7))
print(s.find('Y'))
print(s.format(age=18, addr='甘肃'))
print(s.format_map({'age': 22, 'addr': 'cq'}))
print(s.index('a', 8))
print('18'.isalnum())
print('0010'.isdecimal())
print('123.12'.isdigit())
print('my lover is yang'.replace('lover', 'like'))
print('My title title'.split('i', 2))

# eval
a = str({'beijing': {'No.1': 'GDP'}})
print(type(a))
print(a)

a = eval(a)
print(type(a))
print(a['beijing'])

