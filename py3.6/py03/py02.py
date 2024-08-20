# py3.6_02
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
# 上述算法的效率是O(n)
res = is_prime(11)
print("this is prime number : ", str(res))
