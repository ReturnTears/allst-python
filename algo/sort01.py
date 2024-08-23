# Sort01-冒泡排序
def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index -= 1
    return list
# 上述冒泡排序算法效率：O(N²)
list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(bubble_sort(list))
