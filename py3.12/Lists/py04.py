# Lists
records = [('a', 23), ('b', 56), ('c', 2), ('d', 19), ('e', 70), ('f', 15)]

stack = []
stack.append(1)
stack.append(2) 
stack.pop()
print(stack)

def get_name_and_age():
    name = 'Kang'
    age = 18
    return [name, age]

print(get_name_and_age())

(name, age, sex) = ('KangShuai', 22, 'Male')
print(name, age, sex)

date = (2017, 8, 14)
print('%d-%d-%d' % date)

def get_name_and_age_sex():
    return ('KangKang', 19, 'Male') # this is a tuple


student_info = {('Kang', 18):600,('Wang',20):700}
print(student_info[('Kang', 18)])
