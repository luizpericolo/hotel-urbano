class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y)

if __name__ == "__main__":
    v = Vector(1, 2)
    v2 = Vector(2, 2)
    print(v + v2)
    print(v * 3)
    # print(4 * v) # TypeError: unsupported operand type(s) for *: 'int' and 'Vector'
