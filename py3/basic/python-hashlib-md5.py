# author        JUNN
# since         2019-09-01 下午 02:29
# description   MD5

import hashlib

m = hashlib.md5()
# print(m)

# 转换
m.update('hello world'.encode('utf-8'))
# print(m.hexdigest())

m.update('alex'.encode('utf-8'))
# print(m.hexdigest())

# 上述的两种方式合并为如下
m2 = hashlib.md5()
m2.update('hello worldalex'.encode('utf-8'))
# print(m2.hexdigest())


# sha256
m3 = hashlib.sha256()
m3.update('hello world'.encode('utf-8'))
print(m3.hexdigest())