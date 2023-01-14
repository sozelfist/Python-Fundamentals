def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class MySingletonClass:
    pass


if __name__ == '__main__':

    s1 = MySingletonClass()
    s2 = MySingletonClass()

    assert s1 is s2
