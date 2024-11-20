import re
str = "Python 3.12 is amezing !"
x = re.search("Python", str)
print(x)

res = re.sub("Python", "Coding", str)
res = re.sub("amezing", "funny", res)
print(res)

str = "Hello Python, bye Python!"
res = re.findall("Python", str)
print(res)

