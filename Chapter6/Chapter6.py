from abc import ABCMeta, abstractmethod
from Vector import Vector
from random import uniform
from math import isclose
from CarForSale import CarForSale
from json import loads, dumps
from pathlib import Path
from datetime import datetime, timedelta

    
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

#A1()
#A2()
#A3()
#A4()
#A5()
#A6()
#A7()
#A8()
A9()