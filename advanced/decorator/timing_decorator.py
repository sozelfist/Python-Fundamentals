import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper


@time_it
def my_function():
    time.sleep(2)


if __name__ == '__main__':
    my_function()
