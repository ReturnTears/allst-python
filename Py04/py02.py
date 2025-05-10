# 变长实参
def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
    return maxnum

res = maximum(11,12,3,4,8)
print(res)

