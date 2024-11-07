
def my_func() :
    local_var = "this ia a local variable"
    print(local_var)

global_var = "this ia a global variable"
def my_func2():
    print(global_var)

def my_func3():
    global my_var
    my_var = "this is a new variable"
    print(my_var)

my_func()
my_func2()
my_func3()
