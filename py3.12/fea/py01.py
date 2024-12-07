seq = []
for i in range(1, 11):
    seq.append(i*2)
print(seq)


seqs = [x**2 for x in range(1,11)]
print(seqs)


seqs = [x**2 for x in range(1,11) if x ** 2 > 50]
print(seqs)


nums = [1,2,3,4,5,6,7,8,9,10]
new_nums = [num if num % 2 == 0 else -num for num in nums]
print(new_nums)

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

num_gen = (num for num in nums if num % 2 == 0)
for num in num_gen:
   print(num)

numbers = [1,2,3,4,5]
print(sum(num for num in numbers if num % 2 == 0))

