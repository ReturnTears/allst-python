'''
The 'with' statement ensures that clean-up code is always executed. This helps prevent bugs and leakages, such as
forgetting to close a file that can hog up the memory.
'''
with open('example.txt', 'w') as file:
    file.write('Hello World !')

