'''
Comparison Operators like > < >= <= == != can be overloaded with the special methods __lt__, __le__, __eq__, __ne__, __ge__, __gt__

'''
class Membership:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    def __lt__(self, other):
        return self.duration < other.duration
    
m1 = Membership('Gold', 12)
m2 = Membership('Silver', 6)
print(m1 < m2)
