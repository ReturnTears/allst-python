def greatestNumber(array):
  for i in array:
    # 暂时假定i为最大值：
    isIValTheGreatest = True
    for j in array:
      # 假如发现了比i更大的值，那么i就不再是最大值了：
      if j > i:
        isIValTheGreatest = False
    # 如果检查了所有其他数后，i仍保持最大，那么i就是最大值：
    if isIValTheGreatest:
      return i
# 算法的效率是 O(n²)
array = [1, 2, 3, 4, 5, 6, 17, 8, 9, 10]
res = greatestNumber(array)
print("result is ", res)
