# Nested List
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
print(nested_list)

print(nested_list[0])

print(nested_list[0][1])

for sublist in nested_list:
    for element in sublist:
        print(element)

