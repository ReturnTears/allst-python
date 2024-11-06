# try
numbers = [1,2,3,4,5,6,'seven']
for i in numbers:
    try:
        print(i**2)
    except TypeError:
        print("Error: TypeError")
