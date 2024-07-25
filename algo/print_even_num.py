# method 1
def print_number_v_1():
    number = 2
    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1

# method 2
def print_number_v_2():
    number = 2
    while number <= 100:
        print(number)
    number += 2

# print_number_v_1()
"""
函数2比函数1效率高：
这是因为第一个要循环 100 次，而第二个只要循环 50 次。也就是说，第一个函数执行的步骤数是第二个的两倍。
"""
