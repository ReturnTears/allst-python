# 变量  
a=2
def zhouchang():
    global a
    a = 5
    print('内部a = ', a)
f = zhouchang()
print('外部a = ', a)
