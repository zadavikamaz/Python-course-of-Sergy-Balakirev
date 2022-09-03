class SingletonFive:
    __instance = None
    __cnt = 0

    def __new__(cls, *args, **kwargs):
        if cls.__cnt < 5:
            cls.__instance = super().__new__(cls)
            cls.__cnt += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]

for obj in objs:
    print(obj.name)