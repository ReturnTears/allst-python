import py02
emp = py02.Employee(500)
print(emp.get_id())

# accessing private variable through name mangling
print(emp._Employee__id)
