def number_generator():
    yield 0
    yield 1
    yield 2

gen_result = number_generator()
print(gen_result)
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))

for num in number_generator():
    print(num)
