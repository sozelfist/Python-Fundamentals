class Shape:
    def __init__(self, sides: int):
        self.sides = sides

    def get_sides(self):
        return self.sides

    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self):
        super().__init__(3)

    def draw(self):
        print("Drawing a triangle")


class Rectangle(Shape):
    def __init__(self):
        super().__init__(4)

    def draw(self):
        print("Drawing a rectangle")


class Circle(Shape):
    def __init__(self):
        super().__init__(0)

    def draw(self):
        print("Drawing a circle")


def draw_shape(shape: Shape):
    shape.draw()


if __name__ == '__main__':
    triangle = Triangle()
    rectangle = Rectangle()
    circle = Circle()

    draw_shape(triangle)  # "Drawing a triangle"
    draw_shape(rectangle)  # "Drawing a rectangle"
    draw_shape(circle)  # "Drawing a circle"
