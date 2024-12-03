'''
Arthmetic operators such as +, -, *, /, %, **, // can be overloaded using their respective dunder method. each of them corresponds to a special method: 
__add__(),__sub__(),__mul__(),__truediv__(),__mod__(),__pow__(),__floordiv__()
'''
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i
    def __add__(self, other):
        r = self.r + other.r
        i = self.i + other.i
        return ComplexNumber(r, i)
    
num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(2, 3)
result = num1 + num2
print(result.r, result.i)
