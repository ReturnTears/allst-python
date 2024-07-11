# def
def product(a, b):
    """
    计算两数的乘积
    :param a: 数1
    :param b: 数2
    :return: 两数的乘积
    """
    return a * b, a + b

# call method
result, sum_val = product(3, 5)
print("result =", result)
print("sum_val =", sum_val)

# def default val
def calculate(a=2, b=3):
    return a * b, a + b

val1 = calculate()
print("val1 =", val1)

val2 =  calculate(5, 6)
print("val2 =", val2)
