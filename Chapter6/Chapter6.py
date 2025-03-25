from abc import abstractmethod
from Vector import Vector
from random import uniform
from math import isclose, sin
from CarForSale import CarForSale
from json import loads
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from random import randint

    
class Vec2(Vector):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self, v2):
        return Vec2(self.x + v2.x, self.y + v2.y)
    def scale(self, scalar):
        return Vec2(scalar * self.x, scalar * self.y)
    def __eq__(self,other):
        if(self.__class__ == other.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __repr__(self):
        return "Vec2({},{})".format(self.x,self.y)
    
class Vec3(Vector):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def add(self, v2):
        return Vec3(self.x + v2.x, self.y + v2.y, self.z + v2.z)
    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)
    def __eq__(self,other):
        if(self.__class__ == other.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False
    def __repr__(self):
        return "Vec3({},{},{})".format(self.x,self.y,self.z)

def average(v1,v2):
    return 0.5 * v1 + 0.5 * v2

def random_scalar():
    return uniform(-10, 10)

def random_vec2():
    return Vec2(random_scalar(), random_scalar())

def approx_equal_vec2(v,w):
    return isclose(v.x,w.x) and isclose(v.y,w.y)

for _ in range(0, 100):
    a = random_scalar()
    u, v = random_vec2(), random_vec2()
    assert approx_equal_vec2(a* (u+v), a*v+a*u)

def test(eq, a, b, u, v, w):
    assert eq(u + v, v + u)
    assert eq(u + (v + w), (u + v) + w)
    assert eq(a * (b * v), (a*b)*v)
    assert eq(1 * v, v)
    assert eq((a+b) * v, a * v + b * v)
    assert eq(a*v + a*w, a * (v+w))

for i in range(0,100):
    a,b = random_scalar(), random_scalar()
    u,v,w = random_vec2(), random_vec2(), random_vec2()
    test(approx_equal_vec2,a,b,u,v,w)

def A1():
    print(Vec3(1,2,3) * 4 - Vec3(5,6,7) * 8)

# 구현하긴 했으나 답지보다 많이 부족함. python 문법을 몰라서 문제 조건을 달성했는지도 확인필요.
# 틀린 것으로 봐야함. 그러나 공부 목적에 따라 일단 넘어감.
def CoordinateVector(Vector):
    @abstractmethod
    def demension():
        pass
def A2():
    print("구현함.")

# 구현하긴 했는데 답지보다 부족함.
def A3():
    v = Vec3(1,2,3)
    print(v.zero())
    print(v.negative())

def random_vec3():
    return Vec3(random_scalar(), random_scalar(), random_scalar())
def approx_equal_vec3(v, w):
    return isclose(v.x,w.x) and isclose(v.y,w.y) and isclose(v.z,w.z)
def A4():
    for i in range(0,100):
        a,b = random_scalar(), random_scalar()
        u,v,w = random_vec3(), random_vec3(), random_vec3()
        test(approx_equal_vec3,a,b,u,v,w)

def A5():
    zero=0
    zeroVector=Vec3(1,1,1).zero()
    def test(eq, v):
        assert eq(zeroVector+v, v)
        assert eq(zero*v, zeroVector)
        assert eq(-v + v, zeroVector)
    for i in range(0,100):
        v = random_vec3()
        test(approx_equal_vec3,v)

def A6():
    print(Vec2(1, 2) == Vec3(1,2,3))

def A7():
    print(Vec3(2,4,6)/2)

def testWithZero(zero, eq, a, b, u, v, w):
    test(eq, a, b, u, v, w)
    assert eq(zero+v, v)
    assert eq(0*v, zero)
    assert eq(-v + v, zero)

def A8():
    for i in range(0, 100):
        a, b = random_scalar(), random_scalar()
        u, v, w = random_scalar(), random_scalar(), random_scalar()
        testWithZero(0, isclose, a, b, u, v, w)


# 아래 A9 잘못 풀었음.
contents = Path('./Chapter6/cargraph.json').read_text()
cg = loads(contents)
cleaned = []

def parse_date(s):
    input_format="%Y/%m/%d - %H:%M"
    return datetime.strptime(f"2018/{s}",input_format)
    
    return dt
for car in cg[1:]:
    try:
        row = CarForSale(int(car[1]), float(car[3]), float(car[4]), parse_date(car[6]), car[2],  car[5],  car[7], car[8])
        cleaned.append(row)
    except: pass

cars = cleaned
def A9():
    def approx_equal_time(t1, t2):
        test = datetime.now()
        return isclose((test-t1).total_seconds(), (test-t2).total_seconds())
    def approx_equal_car(u, v):
        return isclose(u.model_year, v.model_year) and isclose(u.mileage, v.mileage) and isclose(u.price, v.price) and approx_equal_time(u.posted_datetime, v.posted_datetime)
    for i in range(0, len(cars)-2):
        a, b = random_scalar(), random_scalar()
        u, v, w = cars[i], cars[i+1], cars[i+2]
        testWithZero(CarForSale.zero(), approx_equal_car,  a, b, u, v, w)

def plot(fs, xmin, xmax):
    xs = np.linspace(xmin,xmax,100)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    for f in fs:
        ys = [f(x) for x in xs]
        plt.plot(xs,ys)
    plt.show()
class Function(Vector):
    def __init__(self, function):
        self.function = function
    def add(self, other):
        def addedFunction(param):
            return self(param) + other(param)
        return Function(addedFunction)
    def scale(self, scalar):
        def scaledFunction(param):
            return self(param) * scalar
        return Function(scaledFunction)
    @classmethod
    def zero():
        def zeroFunction(param):
            return 0
        return Function(zeroFunction)
    def __call__(self, args):
        return self.function(args)
def A10():
    def f_origin(x):
        return 0.5 * x +3
    def g_origin(x):
        return sin(x)
    f = Function(f_origin)
    g = Function(g_origin)
    plot([f,g,f+g,3*g], -10, 10)

def A11():
    print("방법이 떠오르지 않는다.")

def A12():
    def approx_equal_fuction(v, w):
        allSame = True;
        for i in range(0, 100):
            x=random_scalar()
            if(isclose(v(x))):
                allSame=False
                break
        return allSame
    def random_function():
        degree = randint(0,5)
        #p = Polynomial(*[uniform(-10,10) for _ in range(0,degree)])
        #return Function(lambda x: p(x))
    for i in range(0, 100):
        a, b=random_scalar(), random_scalar()
        u, v, w=random_function(), random_function(), random_function()
    testWithZero(Function.zero, approx_equal_fuction, a, b, u, v, w)

class Function2(Vector):
    def __init__(self, function):
        self.function = function
    def add(self, other):
        def addedFunction(param0, param1):
            return self(param0, param1) + other(param0, param1)
        return Function2(addedFunction)
    def scale(self, scalar):
        def scaledFunction(param0, param1):
            return self(param0, param1) * scalar
        return Function2(scaledFunction)
    @classmethod
    def zero():
        def zeroFunction(param0, param1):
            return 0
        return Function2(zeroFunction)
    def __call__(self, *args):
        return self.function(args[0], args[1])
def A13():
    def f_origin(x, y):
        return 0.5 * x +3 + 0.5 * y +3
    def g_origin(x, y):
        return sin(x+y)
    f = Function2(f_origin)
    g = Function2(g_origin)
    x=1
    y=2
    print([f(x,y),g(x,y),(f+g)(x,y),(3*g)(x,y)])
    x=4
    y=5
    print([f(x,y),g(x,y),(f+g)(x,y),(3*g)(x,y)])
    x=-1
    y=-4
    print([f(x,y),g(x,y),(f+g)(x,y),(3*g)(x,y)])
    
def A14():
    print("d")

class Matrix(Vector):
    @classmethod
    def col(cls):
        pass
    @classmethod
    def row(cls):
        pass
class Matrix5_by_3(Matrix):
    @classmethod
    def col(cls):
        return 3
    @classmethod
    def row(cls):
        return 5
    def __init__(self, arg):
        self.arg = arg
    def add(self, other):
        return Matrix5_by_3(tuple(tuple([pair[0] + pair[1] for pair in zip(rowPair[0], rowPair[1])]) for rowPair in zip(self.arg, other.arg)))
    def scale(self, scalar):
        return Matrix5_by_3(tuple(tuple(elmt*scalar for elmt in row) for row in self.arg))
    def __repr__(self):
        return self.arg.__repr__()
    @classmethod
    def zero(cls):
        return Matrix5_by_3(tuple(tuple([0 for j in range(0,3)]) for i in range(0, 5)))
def A15():
    u=Matrix5_by_3(((1,2,3),(4,5,6),(7,8,9),(10, 11,12),(13,14,15)))
    v=Matrix5_by_3(((16,17,18),(19,20,21),(22,23,24),(25,26,27),(28,29,30)))
    print(u)
    print(v)
    print(u+v)
    print(u*3)

def A16():
    def approx_equal_matrix5_by_3(u,v):
        isSame = True
        for row in range(0, 5):
            for col in range(0,3):
                if(isclose(u.arg[row][col], v.arg[row][col])==False):
                    isSame=False
                    break
        return isSame
    def random_matrix5_by_3():
        return Matrix5_by_3(tuple(tuple([random_scalar() for j in range(0,3)]) for i in range(0, 5)))
    for i in range(0, 100):
        a, b = random_scalar(), random_scalar()
        u, v, w = random_matrix5_by_3(), random_matrix5_by_3(), random_matrix5_by_3()
        testWithZero(Matrix5_by_3.zero(), approx_equal_matrix5_by_3, a,b,u,v,w)

#A1()
#A2()
#A3()
#A4()
#A5()
#A6()
#A7()
#A8()
#A9()
#A10()
#A11()
#A12()
#A13()
#A14()
#A15()
A16()