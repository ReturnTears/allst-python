# 该函数会计算数组中任意两数乘积的最大值。
def greatestProduct(array):
    greatestProductSoFar = array[0] * array[1]
    for i, iVal in enumerate(array):
        for j, jVal in enumerate(array):
            if i != j and iVal * jVal > greatestProductSoFar:
                greatestProductSoFar = iVal * jVal
    return greatestProductSoFar
# 算法的效率是 O(n²)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = greatestProduct(array)
print("result is ", res)

