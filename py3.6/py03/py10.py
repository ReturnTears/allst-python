# 优化py09
def greatestNumber(array):
  steps = 0
  maxValue = array[0]
  for i in array:
    steps += 1
    if i > maxValue:
      maxValue = i
  print("Steps : ", steps)
  return maxValue
# 算法的效率是 O(n)
array = [11, 2, 13, 4, 5, 6, 17, 8, 9, 10]
res = greatestNumber(array)
print("result is ", res)
