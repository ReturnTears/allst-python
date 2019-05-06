# python基础(单行注释)
msg = "Hello Python"
print(msg)

''' 
 多行注释
 guess age : 18
 input方法类似Java的System.in
 input 接受的所有数据都是字符串，即便你输入的是数字，但依然会被当成字符串来处理
'''
defAge = 18
flag = True
while flag:
    guessAge = int(input(">>: "))
    if guessAge == defAge:
        print("Yes, You got it")
        flag = False
    elif guessAge > defAge:
        print("should try smaller")
    else:
        print("try bigger")
print("End")

# guess score
score = int(input("score: "))
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("E")

# 循环输出矩形符号
a = 1
while a <= 4:
    b = 1
    while b <= 4:
        print("#", end="")
        b += 1
    print()
    a += 1

