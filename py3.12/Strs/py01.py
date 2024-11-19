greeting = "Hello"
# greeting[0] = 'h' TypeError
print(greeting)

name = "Kang"
greeting = "Halo , {}".format(name)
print(greeting)

greeting = f"Hi , {name}"
print(greeting)

s ="Halo , Python!"
print(s.lower())
print(s.upper())

str = f" {name} is {18} years old."
print(str.strip())

print(s.replace("Halo", "Hi"))

age = 33
str = "{0} is {1} years old".format(name, age)
print(str)

float_num = 3.14159
print(f"{float_num:.2f}")
print("{:.2f}".format(float_num))
print("{:,}".format(123456789))
print("{:*>8}".format("Python"))
print("{:*^8}".format("Python"))

version = 3.1215623
new_version = version + 0.02
print(f"{version},{new_version}")

print(f"{version:.2f}")

string = "Hello, Python 3.12!"
print(string[0])
print(string[-1])
print(string[0:5])
print(string[:5])
print(string[7:])
