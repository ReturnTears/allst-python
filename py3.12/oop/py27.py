class Vector:
    def __init__(self, x):
        self.x = x
    def __neg__(self):
        return Vector(-self.x)

v1 = Vector(5)
v2 = -v1
print(v2.x)
