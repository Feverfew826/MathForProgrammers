from draw3d import *
from draw2d import *
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

def A16():
    print(f"3.61*1.44*cos(101.3/180*pi)={3.61*1.44*cos(101.3/180*pi)}")

def A17():
    polar1=(sqrt(3**2+4**2), atan2(4, 3))
    polar2=(sqrt(4**2+3**2), atan2(3, 4))
    print(f"({polar1[0]}, {polar1[1]}), ({polar2[0]},{polar2[1]})")
    print(f"{polar1[1]}-{polar2[1]}={polar1[1]-polar2[1]}")
    print(f"{polar1[0]*polar2[0]*cos(polar1[1]-polar2[1])}={3*4+4*3}")

def A18():
    print(f"cos(theta)=(1*(-1)+1*(-1)+1*1)/(sqrt(3)*sqrt(3))")
    value=(1*(-1)+1*(-1)+1*1)/(sqrt(3)*sqrt(3))
    print(f"acos(cos(theta))=acos({value})={acos(value)}")
    print(acos(value)/pi*180)

def A19():
    print("오른손 법칙: a, c, d")

def A20():
    print("다르다")

def A21():
    print("+x방향")
    ux=0
    uy=0
    uz=3
    vx=0
    vy=-2
    vz=0
    print(f"(uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx)=({uy*vz-uz*vy},{uz*vx-ux*vz},{ux*vy-uy*vx})")

def A22():
    ux=1
    uy=-2
    uz=1
    vx=-6
    vy=12
    vz=-6
    print(f"(uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx)=({uy*vz-uz*vy}, {uz*vx-ux*vz}, {ux*vy-uy*vx})")

def A23():
    print("u=밑변이라고 하면, 높이는 |v|*sin(theta), 따라서 평행사변형의 면적은 |u|*|v|*sin(theta)")

def A24():
    ux=1
    uy=0
    uz=1
    vx=-1
    vy=0
    vz=0
    print(f"(uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx)=({uy*vz-uz*vy}, {uz*vx-ux*vz}, {ux*vy-uy*vx})")

def A25():
    v=(0,0,1)
    print(cross((0,0,1), v))
    v=(0,0,-1)
    print(cross((0,0,1), v))
    v=(0,-1,0)
    print(cross((0,0,1), v))
    v=(0,1,0)
    print(cross((0,0,1), v))
    v=(1,0,0)
    print(cross((0,0,1), v))
    v=(-1,0,0)
    print(cross((0,0,1), v))
    v=(1,1,1)
    print(cross((0,0,1), v))
    print("(0,0,1)이 z축과 나란하므로, v로 어떤 벡터가 주어지던 z축과 수직이기 위해서는 z값이 0이어야 한다.")

def A26():
    print("dot(cross(u, v), (ux, uy, uz))")
    print("dot((uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx), (ux, uy, uz))")
    print("=(uy*vz-uz*vy)*ux+(uz*vx-ux*vz)*uy+(ux*vy-uy*vx)*uz")
    print("=uy*vz*ux -uz*vy*ux +uz*vx*uy -ux*vz*uy +ux*vy*uz -uy*vx*uz")
    print("=uy*vz*ux -ux*vz*uy +uz*vx*uy -uy*vx*uz +ux*vy*uz -uz*vy*ux")
    print("=uy*vz*ux -uy*vz*ux +uz*vx*uy -uz*vx*uy +ux*vy*uz -ux*vy*uz")
    print("=0=|cross(u,v)|*|v|*cos(theta), cos(theta)=0, theta=90 or 270의 배수")
    print()
    print("dot(cross(u, v), (ux, uy, uz))")
    print("dot((uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx), (vx, vy, vz))")
    print("=(uy*vz-uz*vy)*vx+(uz*vx-ux*vz)*vy+(ux*vy-uy*vx)*vz")
    print("=uy*vz*vx -uz*vy*vx +uz*vx*vy -ux*vz*vy +ux*vy*vz -uy*vx*vz")
    print("=uy*vz*vx -uy*vx*vz +uz*vx*vy -uz*vy*vx +ux*vy*vz -ux*vz*vy")
    print("=uy*vz*vx -uy*vz*vx +uz*vx*vy -uz*vx*vy +ux*vy*vz -ux*vy*vz")
    print("=0=|cross(u,v)|*|v|*cos(theta), cos(theta)=0, theta=90 or 270의 배수")

def A27():
    midPoints=[(-1,-1,0), (1,-1,0), (-1,1,0), (1,1,0)]
    topPoint=(0,0,3)
    bottomPoint=(0,0,-3)
    topSegments=[Segment3D(topPoint, midPoint) for midPoint in midPoints]
    bottomSegments=[Segment3D(bottomPoint, midPoint) for midPoint in midPoints]
    midSegments=[
        Segment3D(midPoints[0], midPoints[1]),
        Segment3D(midPoints[0], midPoints[2]),
        Segment3D(midPoints[3], midPoints[1]),
        Segment3D(midPoints[3], midPoints[2])
        ]
    segments=topSegments+bottomSegments+midSegments
    draw3d(*segments)

def A28():
    print("그렇지 않다. [(0,1,0), (0,0,1), (1,0,0)], [(0,0,1), (1,0,0), (0,1,0)]이 있다.")

octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

# u와 v의 내적을 v의 길이로 나누면, u의 v성분을 알 수 있다.
# u와 v의 사잇각이 theta일 때, u와 v를 평면상에 그려보면(이때, v를 밑변으로 둔다.), 결국 우리가 구하고자 하는 길이는 |u|cos(theta)라는 것을 알 수 있다(u에서 수선의 발을 내려보면 알 수 있다.).
# 그리고 |u|cos(theta)를 쉽게 구하는 방법은 내적(|u||v|cos(theta))에서 |v|를 나누는 것이다.
def component(v,direction):
    return (dot(v,direction) / length(direction))

# 수직인 벡터 2개를 축으로 정하고, 각 축에 대한 성분을 구하는 것으로 3차원을 2차원에 투영(직교 투영)할 수 있다.
# 여기서는 x축, y축과 나란한 벡터인 (1,0,0), (0,1,0)을 이용해 x성분과 y성분을 구한다. 즉 xy평면에 투영한다.
def vector_to_2d(v):
    return (component(v, (1,0,0)), component(v, (0,1,0)))

# 면을 이루는 각 점을 xy평면에 투영한다.
def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]

blues = matplotlib.colormaps.get_cmap('Blues')

# 단위 벡터로 변환
def unit(v):
    return scale(1./length(v), v)

# 면의 두 선분에 대한 벡터를 구하고, 그것의 외적을 구하는 것으로 면에 수직인 normal vector를 얻는다.
def normal(face):
    return cross(subtract(face[1], face[0]), subtract(face[2], face[0]))

# 면이 보이는 지를 normal의 z성분으로 확인하고(xy 평면 투영이기 떄문에), 그림자를 normal과 light의 내적으로 계산한다. 그림자 값으로 채워진 Polygon2D들을 모아다가 그린다.
def renderSample(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons=[]
    for face in faces:
        unit_normal = unit(normal(face))
        normal_z = unit_normal[2]
        if normal_z > 0:
            c = color_map(1- dot(unit_normal, unit(light)))
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            polygons.append(p)
    draw2d(*polygons, axes=False, origin=False, grid=None)

# 아래는 책의 소스 코드에서 제공하는 구체의 면을 만드는 코드. 책에서도 다루지 않아서 이해하고 넘어가지 않고 그냥 넘어감. 나중에 한번 보면 좋을 것 같음.
def split(face):
    midpoints = [unit(add(face[i], face[(i+1)%len(face)])) for i in range(0,len(face))]
    triangles = [(face[i], midpoints[i], midpoints[(i-1)%len(face)]) for i in range(0,len(face))]
    return [midpoints] + triangles

def rec_split(faces, depth=0):
    if depth == 0:
        return faces
    else:
        return rec_split([new_face for face in faces for new_face in split(face)], depth-1)

# NICE SPHERE!
def sphere_approx(n):
    return rec_split(octahedron,n)


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
#A23()
#A24()
#A25()
#A26()
#A27()
#renderSample(octahedron)
#renderSample(sphere_approx(3))