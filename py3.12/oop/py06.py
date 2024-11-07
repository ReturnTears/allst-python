
def sum_nums(a, b):
    return a + b

result = 0
def add_to_result(a):
    global result
    result += a

add_to_result(sum_nums(3, 5))
print(result)
