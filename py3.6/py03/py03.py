# py3.6_03
def isLeapYear(year) :
    if (year % 100 == 0) :
       return (year % 400 == 0)
    else:
       return (year % 4 == 0)

# 上述算法的效率是O(1)
res = isLeapYear(2021)
print("this year is Leap : ", str(res))
