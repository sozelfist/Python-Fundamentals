class Shape:
    def __init__(self, sides: int):
        self.sides = sides

    def get_sides(self):
        return self.sides


class Triangle(Shape):
    def __init__(self):
        super().__init__(3)


class Rectangle(Shape):
    def __init__(self):
        super().__init__(4)


class Circle(Shape):
    def __init__(self):
        super().__init__(0)


if __name__ == '__main__':
    triangle = Triangle()
    print(triangle.get_sides())  # 3
    rectangle = Rectangle()
    print(rectangle.get_sides())  # 4
    circle = Circle()
    print(circle.get_sides())  # 0
