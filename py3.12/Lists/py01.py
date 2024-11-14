# Lists
groceries = ['apples','bananas','carrots']
print(groceries)
print(groceries[0])

# append
groceries.append('milk')
print(groceries)

# insert
groceries.insert(1,'oranges')
print(groceries)

# extend
other_fruit = ['grapes','pears']
groceries.extend(other_fruit)
print(groceries)

# remove
groceries.remove('oranges')
print(groceries)

# pop
popped_item = groceries.pop()
print(popped_item)
print(groceries)

# index
idx = groceries.index('milk')
print(idx)

# count : count()函数返回列表中指定元素的出现次数。
cnt = groceries.count('milk')
print(cnt)

# sort
groceries.sort()
print(groceries)

# reverse
groceries.reverse()
print(groceries)

# clear
groceries.clear()
print(groceries)
