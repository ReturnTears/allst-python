# 🍎 Looping with for and while loops

animals = {"cat":"miaomiao", "dog":"wangwang", "bird":"jijizhazha"}
for key, value in animals.items(): 
    print(f"{key} is {value}.")

for key in animals: 
    print(f"{key} is {animals[key]}.")

