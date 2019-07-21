# author        JUNN
# since         2019-07-21
# description   time模块

import time, datetime

# print(help(time))
# 时间戳(1970 ~ 至今)
# print(time.time())
# clock
# time.sleep(3)
# 计算CPU执行时间
# print(time.clock())
# 结构化时间
# print(time.gmtime())
# 本地时间
# print(time.localtime())
# 自定义日期格式
struct_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))
# 将日期转换为格式化日期
print(time.strptime('2019-07-21 23:04:46', '%Y-%m-%d %H:%M:%S'))
a = time.strptime('2019-07-21 23:04:46', '%Y-%m-%d %H:%M:%S')
print(a.tm_year)

print(time.ctime())
# 转换为时间戳
print(time.mktime(time.localtime()))

print(datetime.datetime.now())

