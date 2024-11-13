square = lambda x: x ** 2
print(square(5))

students = [("kang", 18), ("lee", 20), ("choi", 19)]
students.sort(key=lambda x: x[1])
print(students)

books = [
    {"name": "python", "price": 100},
    {"name": "java", "price": 400},
    {"name": "c++", "price": 200},
    {"name": "javascript", "price": 300},
    {"name": "golang", "price": 800},
    {"name": "scala", "price": 600}
]
books.sort(key=lambda x: x["price"])
print(books)

# map
numbers = [1,2,3,4,5,6,7,8,9,10]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))

# filter
even_nums = filter(lambda x: x % 2 == 0, numbers)
print(list(even_nums))

# reduce
from functools import reduce
product = reduce(lambda x,y : x * y, numbers)
print(product)

# len
words = ["verygood", "world", "python"]
words.sort(key=lambda word:len(word))
print(words)


def square(n):
    return n ** 2

numbers = [1,2,3,4,5]
squares = map(square, numbers)
print(list(squares))

def multiply(x, y):
    return x * y
product = reduce(multiply, numbers)
print(product)
