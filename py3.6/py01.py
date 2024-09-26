def power(a, b = 2):
    r = 1
    while b > 0:
        r = r * a
        b = b - 1
    return r        

# print(power(2, 3)) # 8
print(power(2, 4)) # 16
