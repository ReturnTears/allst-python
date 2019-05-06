# 字典,无序的, 键不能是可变类型,即键唯一 字典是可变类型
dict1 = {'name': 'yang', 'age': 18, 'sex': 'girl', 1: 'ok'}

print(dict1['name'])

dict2 = dict((('lover', 'xiaohu'), ('age', 22)))
dict3 = dict((('name', 'xiaohu'), ))
dict3['addr'] = '嘉峪关'
# setdefault方法,键存在，不做任何修改, 返回值, 键不存在, 新增
dict3.setdefault('name', 'yangYang')
print(dict3)
print(dict3.keys())
print(dict3.values())
print(dict3.items())

dict1.update(dict2)
print(dict1)

