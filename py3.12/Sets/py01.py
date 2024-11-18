primes = {2,3,5,7,11,13}
print(primes)

numbers = set([1,2,3,4,5,6,4,3,2])
print(numbers)

primes.add(17)
print(primes)

primes.remove(11)
print(primes)

odds = {1,3,5,7,9}
inter = primes & odds
print(inter)

print(2 in inter)
print(3 in inter)

for num in inter:
    print(num)

