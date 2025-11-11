import math


class ComplexNumber:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """[X1,Y1] + [X2,Y2] = [X1 + X2, Y1 + Y2]"""
        if isinstance(other, ComplexNumber):
            new_val1 = self.x + other.x
            new_val2 = self.y + other.y
            return ComplexNumber(new_val1, new_val2)
        return NotImplemented
    
    def __mul__(self, other):
        """[X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]"""
        if isinstance(other, ComplexNumber):
            new_val1 = self.x * other.x - self.y * other.y
            new_val2 = self.x * other.y + self.y * other.x
            return ComplexNumber(new_val1, new_val2)
        return NotImplemented
    
    def __truediv__(self, other):
        """[X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]"""
        if isinstance(other, ComplexNumber):
            new_val1 = math.trunc(self.x / other.x)
            new_val2 = math.trunc(self.y / other.y)
            return ComplexNumber(new_val1, new_val2)
        return NotImplemented
