# 统计1的个数
def count_ones(outer_array):
  count = 0
  for inner_array in outer_array:
    for number in inner_array:
      if number == 1:
        count += 1
  return count
# 外层循环遍历的是内层数组，而内层循环遍历的是实际的数。一共有多少数，内层循环就会运行多少次。
# 因此，我们可以说N表示数字的数量。因为算法实际上只是遍历每个数，所以该函数的时间复杂度是O(N)。
array = [[1,2,3],[4,5,6],[7,8,9]]
print(count_ones(array))
