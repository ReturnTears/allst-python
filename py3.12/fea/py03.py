'''
new_list = [expression for member in iterable (if conditional)]
'''

squares = [x**2 for x in range(10)]
print(squares)

print('--------------------------------')

def gen_squares(n):
    for x in range(n):
        yield x**2
squares = gen_squares(10)
for x in squares:
    print(x)

