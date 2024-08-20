# py3.6_04
def arrSum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum
# 上述算法的效率是O(n)
arr = [1,2,3,4,5,6,7,8,9,10,11]
res = arrSum(arr)
print("this array sum : ", res)
