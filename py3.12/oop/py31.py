from functools import total_ordering
@total_ordering
class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self,other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self,other):
        if isinstance(other, self.__class__):
            return (self.x , self.y) < (other.x , other.y)
        return NotImplemented
