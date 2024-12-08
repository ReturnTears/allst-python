import time
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('spend %s' %(end_time - start_time))
        return result
    return wrapper

@time_decorator
def simulated_process():
    time.sleep(1)

simulated_process()

