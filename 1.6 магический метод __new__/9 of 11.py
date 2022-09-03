class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

    # что бы скопировать весь словарь в случае большого количества значений
    # при этом мы можем клонировать pt после добавления иных координат pt.z = 0
    # 1)
    # def clone(self):
    #     new_clone = super().__new__(type(self))
    #     new_clone.__dict__.update(self.__dict__)
    #     return new_clone
    # 2)
    # def clone(self):
    #     return type(self)(**self.__dict__)
    # 3)
    # def clone(self):
    #     return Point(**self.__dict__)
    # 4)
    # def clone(self):
    #     new = Point()
    #     new.__dict__ = self.__dict__
    #     return new


pt = Point(1, 2)
pt_clone = pt.clone()

print(type(pt))
