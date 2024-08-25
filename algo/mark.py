# 只有当两个循环运行次数都和N有关时，嵌套循环才会让算法复杂度变为O(N2)。
def mark_inventory(clothing_items):
  clothing_options = []
  for item in clothing_items:
  # 遍历尺寸1~5（Python的range到第二个数为止，但不包括第二个数）：
    for size in range(1, 6):
        clothing_options.append(item + " Size: " + str(size))
  return clothing_options

# 上述算法：尽管外层循环运行了N次，但内层循环只运行了5次。换言之，无论N的值是多少，内层循环都只运行5次。
# 时间复杂度可以简化为O(N)
items = ["Purple Shirt", "Yellow Shirt"]
result = mark_inventory(items);
print(result)
