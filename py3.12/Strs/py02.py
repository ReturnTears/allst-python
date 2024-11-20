dt = "2024-01-01"
print(dt)
year,month,day = dt[:4],dt[5:7],dt[8:]
print(year,month,day)

str = "weolcome to python"
print(str.capitalize())
print(str.title())

extra_str = "  Hello, Python !   "
print(extra_str.strip())


str = "###Python##"
print(str.strip("#"))

str = "I like Python 2.7 ~"
print(str.replace("2.7", "3.12"))

str = "Python 3.12 is amezing !"
res = str.split(" ")
print(res)

str = ",".join(res)
print(str)
