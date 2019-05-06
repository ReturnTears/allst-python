# list
# count 统计
t = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
print(t)

# index 索引位置, 从0开始
a = ['wuchao', 'jinxin', 'xiaohu', 'sanpang', 'ligang', 'xiaohu']
print(a.index('xiaohu'))
first = a.index('xiaohu')
end = a[first+1:]
print(end.index('xiaohu'))
print(a.index('xiaohu') + 1 + end.index('xiaohu'))

# reverse 倒序
a.reverse()
print(a)

# sort 数字、字符串(按ASCII码)排序
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)

