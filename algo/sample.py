# 数组抽样:从数组中抽取小块样本,因为输入数组预期会很大，所以只取数组的第一个、最中间的那个以及最后一个值。
def sample(array):
  first = array[0]
  middle = array[int(len(array) / 2)]
  last = array[-1]
  return [first, middle, last]

# 上述算法是O(1)算法
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sample(array)
print(result)
