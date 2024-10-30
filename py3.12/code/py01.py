# Py3.12-dict
persona = {"name":"Kang","origin":"Netherlands","year":1999}
print(type(persona)) # <class 'dict'>

# Py3.12-tuple
coordinates = (4,5)
print(type(coordinates)) # <class 'tuple'>

# Py3.12-dynamic typing
a = 5
print(type(a))
a = "Hello"
print(type(a))

# Py3.12-f-string
name = "Kang"
print(f"Hello {name}", name.upper())
print(f"{name} is {len(name)} characters long")