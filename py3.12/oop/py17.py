class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

v1 = Vector(2, 3)
v2 = Vector(1, 4)
result = v1 + v2
print(result.x, result.y)

