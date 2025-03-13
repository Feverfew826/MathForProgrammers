from draw3d import *
from vectors import *
from math import sin, cos, pi

# 연습장에 손으로 그렸음
def A1():
    draw3d(Points3D((-1, -2, 2)), Arrow3D((-1, -2, 2)), Box3D(-1, -2, 2))

def A2():
    points=[
        (1,1,1),
        (-1,1,1), (1,-1,1), (1,1,-1),
        (-1,-1,1),(-1,1,-1),(1,-1,-1),
        (-1,-1,-1)
    ]
    segments=[]
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if(distance(points[i], points[j])==2):
                segments+=[Segment3D(points[i], points[j])]
    draw3d(
        Points3D(*points),
        *segments
    )

def A3():
    draw3d(Arrow3D((4,0,3)),Arrow3D((-1,0,1)),Arrow3D(add((4,0,3), (-1,0,1)), (4,0,3)),Arrow3D(add((4,0,3), (-1,0,1)), (-1,0,1)), Arrow3D(add((4,0,3), (-1,0,1))))
    print(f"(4,0,3)+(-1,0,1)=(3,0,4)={add((4,0,3),(-1,0,1))}")

def A4():
    print("zip(*vectors1)=[(1,6), (2,7), (3,8), (4,9), (5,10)]")
    print("zip(*vectors1)=[(1,3,5), (2,4,6)]")

def A5():
    vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0, 24)]
    print(add(*vs))
    draw3d(*[Arrow3D(add(*[vs[j] for j in range(0, i+1)]), add(*[(0,0,0)]+[vs[j] for j in range(0, i)])) for i in range(0, len(vs))])

def scale(scaler, vector):
    return tuple(v*scaler for v in vector)
def A6():
    print(f"{scale(3,(1,2,3,4,5))}")

def A7():
    u=(1,-1,-1)
    v=(0,0,2)
    print(add(u,scale(1/2, subtract(v,u))))

def A8():
    print(f"{sqrt(1**2+1**2)} = root of 2")
    print(f"{sqrt(1**2+1**2+1**2)} = root of 3")
    print(f"{sqrt(1**2+1**2+1**2+1**2)} = root of 4")

def A9():
    print("13**2=3**2+4**2+12**2")
    print("4*13**2=4*3**2+4*4**2+4*12**2")
    print("sqrt(4*13**2)=26")
    print("sqrt(4*3**2)=6")
    print("sqrt(4*4**2)=8")
    print("sqrt(4*12**2)=24")
    print(sqrt(6**2+8**2+24**2))

def A10():
    questionLength=length((-1,-1,2))
    print(questionLength)
    print(length((-1/questionLength,-1/questionLength,2/questionLength)))

def A11():
    print("dot(u,v)>dot(v,w)>dot(u,w)")

def A12():
    print(-1*1+-1*2+1*1)
    print("90도보다 크다")

def A13():
    print("dot(u,v)=u1*v1+u2*v2+u3*v3")
    print("dot(2u,v)=(2*u1)*v1+(2*u2)*v2+(2*u3)*v3=2*u1*v1+2*u2*v2+2*u3*v3")
    print("dot(u,2v)=u1*(2*v1)+u2*(2*v2)+u3*(2*v3)=2*u1*v1+2*u2*v2+2*u3*v3")
    print("2*dot(u,v)=2*(u1*v1+u2*v2+u3*v3)=2*(u1*v1)+2*(u2*v2)+2*(u3*v3)")

def A14():
    print("dot(u,u)=u1*u1+u2*u2+u3*u3")
    print("length(u)=sqrt(u1*u1+u2*u2+u3*u3)")
    print("length(u)**2=u1*u1+u2*u2+u3*u3=dot(u,u)")

def A15():
    print("dot(u,v)=|u|*|v|*cos(theta)=21, cos(theta)=1")
    print("dot(u,v)=|u|*|v|*cos(theta)=-21, cos(theta)=-1")
    print("-1<=cos(theta)<=1, -21<=3*7*cos(theta)<=21")

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