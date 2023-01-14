def cache(func):
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        return wrapper.cache[args]
    wrapper.cache = {}
    return wrapper


@cache
def my_function(x):
    print("computing")
    return x * x


if __name__ == '__main__':
    print(my_function(5))  # computing and 25
    print(my_function(5))  # 25
    print(my_function(6))  # computing and 36
