# 9 * 9 正序输出
# x = 1
# while x <= 9:
#     tmp = 1
#     while tmp <= x:
#         print(str(tmp)+"*"+str(x) + "="+str(tmp*x), end="\t")
#         tmp += 1
#     print()
#     x += 1
# # 9 * 9 倒序输出
# y = 9
# while y >= 1:
#     temp = 1
#     while y >= temp:
#         print(str(temp)+"*"+str(y) + "=" + str(temp*y), end="\t")
#         temp += 1
#     print()
#     y -= 1

# 完整格式输出九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("%d*%d=%2d" % (i, j, i*j), end=" ")
#     print("")

# 左上三角格式输出九九乘法表
# for i in range(1, 10):
#     for j in range(i, 10):
#         print("%d*%d=%2d" % (i, j, i*j), end=" ")
#     print("")

# # 右上三角格式输出九九乘法表
# for i in range(1, 10):
#     for k in range(1, i):
#         print(end="         ")
#         for j in range(i, 10):
#             print("%d*%d=%2d" % (i, j, i*j), end="")
#     print("")

# 左下三角格式输出九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d*%d=%2d" % (i, j, i*j), end=" ")
#     print(" ")

# 右下三角格式输出九九乘法表
for i in range(1, 10):
    for k in range(1, 10-i):
        print(end="       ")
        for j in range(1, i+1):
            product = i*j
            print("%d*%d=%2d" % (i, j, product), end=" ")
    print(" ")


