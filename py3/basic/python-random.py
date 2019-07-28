# author        JUNN
# since         2019-07-27 下午 09:11
# description   随机数模块

import random

# 0 ~ 1之间的随机数
print(random.random())


# [1, 7]
# print(random.randint(1, 7))
# print(random.choice('Hello'))
# print(random.choice(['123', 4, [1, 2]]))
# shuffle表示洗牌
# print(help(random.shuffle))
# 从序列中返回两个值
# print(random.sample(['123', 4, [5, 6]], 2))
# [1, 10)
# print(random.randrange(1, 10))


# 定义一个验证码函数(随机生成0-9/A-Z之间的5位随机数)
def var_code():
    code = ''
    for i in range(5):
        num = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(num)
    print(code)


var_code()
