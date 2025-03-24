from abc import ABCMeta, abstractmethod

class Vector(metaclass=ABCMeta):
    @abstractmethod
    def scale(self,scalar):
        pass
    @abstractmethod
    def add(self,other):
        pass
    def __add__(self, other):
        return self.add(other)
    def __mul__(self,scalar):
        return self.scale(scalar)
    def __rmul__(self,scalar):
        return self.scale(scalar)
    def subtract(self,other):
        return self.add(-1 * other)
    def __sub__(self,other):
        return self.subtract(other)
    def __truediv__(self,scalar):
        return self.scale(1.0/scalar)
    # 답지보다 부족함.
    def zero(self):
        return self*0
    def __neg__(self):
        return self * -1