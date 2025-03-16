from vectors import *
from teapot import *
from draw_model import *
from draw2d import *
from hypothesis import given
from hypothesis.strategies import decimals

def translate_by(translation):
    def translate(vector):
        return add(vector, translation)
    return translate    
def A1():
    translate=translate_by((1,2,3)) 
    print(translate((-2,-2,-2)))

def A2():
    draw_model(polygon_map(translate_by((0,0,-20)), load_triangles()))
    print("멀어졌다.")

def A3():
    draw_model(load_triangles())
    draw_model(polygon_map(scale_by(0.5), load_triangles()))
    print("작아진다.")
    draw_model(polygon_map(scale_by(-1), load_triangles()))
    print("점대칭 반대가 된다.")

def A4():
    draw_model(polygon_map(compose(translate_by((-1,0,0)), scale_by(2)), load_triangles()))
    draw_model(polygon_map(compose(scale_by(2), translate_by((-1,0,0))), load_triangles()))
    print("원점과 찻 주전자의 중심 간의 거리가 2배가 된다.")

def A5():
    draw_model(polygon_map(compose(scale_by(0.4), scale_by(1.5)), load_triangles()))
    print("0.6배 스케일의 찻주전자가 된다.")

def compose(*args):
    def composed(vectors):
        returnVectors=vectors
        for arg in reversed(args):
            returnVectors=arg(returnVectors)
        return returnVectors
    return composed
def A6():
    draw_model(load_triangles())
    draw_model(polygon_map(compose(translate_by((-1,0,0)), rotate_y_by(1/2*pi), scale_by(0.5)), load_triangles()))

# 모르겠어서 답지 봄.
def curry2(f):
    def curried1(x):
        def curried2(y):
            return f(x, y)
        return curried2
    return curried1
def A7():
    scale_by = curry2(scale)
    print(scale_by(2)((1,2,3)))

# 문제에서 주어진 대로 회전해 보았으나, x90, z90회전이 y90회전이 되진 않았다.
# 내가 뭘 잘못한걸까?
def A8():
    print("x축 중심으로 90도 회전한 뒤, z축 중심으로 90도 회전시킨다")
    print("z축 중심으로 90도 회전한 뒤, x축 중심으로 90도 회전시킨다")
    
    draw_model(polygon_map(compose(rotate_z_by(1/2*pi), rotate_x_by(1/2*pi)), load_triangles()))
    draw_model(polygon_map(compose(rotate_x_by(1/2*pi), rotate_z_by(1/2*pi)), load_triangles()))
    draw_model(polygon_map(rotate_y_by(1/2*pi), load_triangles()))
    draw_model(polygon_map(rotate_y_by(-1/2*pi), load_triangles()))

def stretch_x(scalar, vector):
    return tuple([vector[0] * scalar] + [vector[i] for i in range(1, len(vector))])
def stretch_by(scalar):
    def curry(vector):
        return stretch_x(scalar, vector)
    return curry
def A9():
    print(stretch_x(3, (1,2,3)))
    print(stretch_by(3)((1,2,3)))

def A10():
    print("S(s*v)=((s*x)**2, (s*y)**2)=((s**2)*(x**2), (s**2)*(y**2))")
    print("s*S(v)=s*(x**2, y**2)=(s*(x**2), s*(y**2))")

def A11():
    print("S(zeroVector)=(x, y, z) 일 때(x 또는 y 또는 z는 0이 아님),")
    print("s*S(zeroVector)=s*(x, y, z)")
    print("S(s*zeroVector)=S(zeroVector)이므로,")
    print("s*S(v) = S(s*v)가 성립하지 않는다.")

def A12():
    print("s*I(v)=s*v, I(s*v)=s*v")
    print("I(u+v)=u+v, I(u)+I(v)=u+v")

def A13():
    print((1.5, 2))
    draw2d(*[Points2D((5,3), color=blue), Points2D((-2,1), color=red), Points2D((1.5, 2))])

def A14():
    src=Points2D(*[(x,y) for x in range(0, 6) for y in range(0, 6)])
    dst=Points2D(*[(vector[0]**2, vector[1]**2) for vector in src.vectors], color=red)
    draw2d(*[src, dst])
    print("일정하던 간격이, 원본의 x, y에 비례해 커진다.")

# A15는 건너뜀.
def A15():
    return

def reflect_x(vector):
    x, y = vector
    return (x, -y)
def A16():
    v1=(1,1)
    v2=(2,1)
    draw2d(*[Arrow2D(v1,color=blue),Arrow2D(v2,color=red),Arrow2D(add(v1, v2),color=black),Arrow2D(reflect_x(v1),color=blue),Arrow2D(reflect_x(v2),color=red),Arrow2D(reflect_x(add(v1, v2)),color=black)])
    draw2d(*[Arrow2D(v1,color=blue),Arrow2D(scale(2, v1),color=black),Arrow2D(reflect_x(v1),color=blue), Arrow2D(reflect_x(scale(2, v1)),color=black)])

def A17():
    print("S(T(u))+S(T(v)) = S(T(u)+T(v)) = S(T(u+v))")
    print("s*S(T(u)) = S(s*T(u)) = S(T(s*u))")

def A18():
    print(rotate_x_by(pi/2)((1,0,0)))
    print(rotate_x_by(pi/2)((0,1,0)))
    print(rotate_x_by(pi/2)((0,0,1)))

def linear_combination(scalars, *vectors):
    multiplies=[scale(scalars[i], vectors[i]) for i in range(0, len(scalars))]
    return add(*multiplies)
def A19():
    print(linear_combination([1,2,3], (1,0,0), (0,1,0), (0,0,1)))

def transform_standard_basis(transform):
    return(transform((1,0,0)), transform((0,1,0)), transform((0,0,1)))
def A20():
    print(transform_standard_basis(translate_by((2,0,0))))

def A21():
    print("(0,0,-1) + (2,1,0) + (-2,0,-2) = (0,1,-3)")

# 연습장에 길게 풀었음
def A22():
    print("A(B(e1))=(0,1,1)")
    print("A(B(e2))=(3,2,1)")
    print("A(B(e3))=(-1,-2,-2)")

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
#A16()
#A17()
#A18()
#A19()
#A20()
#A21()
#A22()