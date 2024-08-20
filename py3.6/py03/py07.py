# py3.6_07
import math
def median(array) :
    middle = math.floor(len(array) / 2)
    if (len(array) % 2 == 0) : # 如果数组有偶数个数：
        return (array[middle - 1] + array[middle]) / 2
    else: # 如果数组有奇数个数
        return array[middle]
# 上述的函数会计算有序数组的中位数
# 上述算法的效率是O(LogN)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = median(arr)
print(res)
