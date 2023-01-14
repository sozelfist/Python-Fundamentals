def check_permission(role):
    return True if role.lower() in ['admin', 'user'] else False


def permission(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if check_permission(role):
                return func(*args, **kwargs)
            else:
                raise PermissionError("you don't have the permission")
        return wrapper
    return decorator


@permission("admin")
def my_function():
    print("Welcome admin")


@permission("user")
def my_function2():
    print("Welcome user")


if __name__ == '__main__':
    my_function()
    my_function2()
