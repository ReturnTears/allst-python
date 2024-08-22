# 插入排序
def insertion_sort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        array[position + 1] = temp_value
    return array
# 上述插入排序算法效率：O(N²)
array = [11, 2, 13, 4, 15, 6, 17, 8, 9, 10]
result = insertion_sort(array)
print("result : ", result)

