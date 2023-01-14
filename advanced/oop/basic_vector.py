class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1 + v2)  # (4, 6)
    print(v1 - v2)  # (-2, -2)
    print(v1 * 2)  # (2, 4)
