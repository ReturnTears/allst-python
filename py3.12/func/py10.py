# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial2(n):
    return 1 if n == 0 else n * factorial2(n-1)

print(factorial2(5))
