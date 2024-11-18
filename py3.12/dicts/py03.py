person = {
    'name': 'John',
    'age': 18,
    'gender': 'male',
    'skill': ['python', 'java']
}

stu = [{'name': 'zhangsan','age': 18},{'name': 'lisi', 'age': 19}, {'name': 'wangwu', 'age': 19}]
grouped = {}
for s in stu:
    age = s['age']
    if age not in grouped:
        grouped[age] = []
    grouped[age].append(s)
print(grouped)
