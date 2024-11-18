def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n <= 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return memo[n]

print(fib(10))