def type_check(func):
    def wrapper(*args, **kwargs):
        for i, (arg, arg_type) in enumerate(zip(args, func.__annotations__.values())):
            if not isinstance(arg, arg_type):
                raise TypeError(

                    f"Argument {i+1} of {func.__name__} should be {arg_type}, not {type(arg)}")
        return func(*args, **kwargs)

    return wrapper


@type_check
def my_function(a: int, b: str) -> str:
    return f"{a} and {b}"


if __name__ == '__main__':
    my_function(10, "Hello")
