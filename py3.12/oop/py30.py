class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return (self.x , self.y) < (self.x , other.y)
        return NotImplemented

p1 = Coordinate(1, 1)
p2 = Coordinate(2, 2)
p3 = Coordinate(1, 1)
print(p1 == p2)
print(p1 == p3)
print(p1 < p2)
