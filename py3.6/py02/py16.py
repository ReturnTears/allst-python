# 嵌套列表与深复制
m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(m[1])
print(m[1][1])

nested = [0]
original = [nested, 1]
print(original)
nested[0] = 'Zero'
print(original)
original[0][0] = 'ZERO'
print(original)
# nested被赋为另一个列表,则变量original和nested之间的关联就断开了
nested = [1, 2, 3, 4, 5, 6, 7, 8]
print(original)

shallow = original[:]
print(shallow)

import copy
list = [[0,1], 2, 3]
deep = copy.deepcopy(list)
print(deep)
list[0][0] = 'zero'
print(list)
print(deep)
