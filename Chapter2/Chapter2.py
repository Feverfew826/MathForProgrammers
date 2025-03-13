from vector_drawing import *
from math import sin
from math import cos
from math import tan
from math import atan
from math import atan2
from vectors import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def A2_1():
    print("x좌표: -1, y좌표: -4")

def A2_2():
    draw(Arrow((2, -2)))

def A2_3():
    # 원래는 좌표를 일일히 써야하는 문제이나, 필요와 편의상 다음으로 대체함.
    for i in range(7, 21):
        print(dino_vectors[i])

def A2_4():
    draw(Polygon(*dino_vectors))

def A2_5():
    draw(Points(*[(x,x**2) for x in range(-10, 11)]))

def A2_6():
    print("u+v=(-0.5,1.5)")
    print("v+w=(5.5,2.5)")
    print("u+w=(2,1)")
    print("u+v+w=(3.5,2.5)")

def add(vectors):
    return (sum([vector[0] for vector in vectors]), sum([vector[1] for vector in vectors]))
def A2_7():
    print(add([(1,2), (2,4), (3,6), (4,8)]))

def translate(translation, vectors):
    return [add([vector, translation]) for vector in vectors]
def A2_8():
    print(translate((1,1), [(0,0), (0,1), (-3,-3)]))

def A2_9():
    print("u+v == (u.x+v.x, u.y+v.y) == (v.x+u.x, v.y+u.y) == v+u")

def A2_10():
    print("가장 긴 화살표: v, w 조합")
    print("가장 짧은 화살표: u, v 조합")

def A2_11():
    dinoGap=12
    translatedDinos = [[(x+i%10*dinoGap,y+(int(i/10)*dinoGap)) for x, y in dino_vectors] for i in range(0, 100)]
    polygons = [Polygon(*translatedDino) for translatedDino in translatedDinos]
    draw(*polygons)

def A2_12():
    added = add([(3,-2), (1,1), (-2,-2)])
    if(abs(added[0]) > abs(added[1])):
        print("x성분이 더 길다.")
    elif(abs(added[0]) < abs(added[1])):
        print("y성분이 더 길다.")
    else:
        print("x성분과 y성분의 길이가 같다.")

def A2_13():
    added = add([(-6,-6), (5,-12)])
    print("(-6,-6): x성분: (-6,0)")
    print("(-6,-6): y성분: (0,-6)")
    length = sqrt((-6)**2 + (-6)**2)
    print("(-6,-6): 길이: ", length)

    print("(5,-12): x성분: (5,0)")
    print("(5,-12): y성분: (0,-12)")
    length = sqrt(5**2 + (-12)**2)
    print("(5,-12): 길이: ", length)

def length(vector):
    return sqrt(vector[0]**2 + vector[1]**2)
def A2_14():
    print(sqrt(35), " ", -sqrt(35))

def A2_15():
    maxVector=dino_vectors[0]
    maxLen = 0
    for elmt in dino_vectors:
        len = length(elmt)
        if(len > maxLen):
            maxLen = len
            maxVector = elmt
    print(maxVector)

def A2_16():
    w=(sqrt(2),sqrt(3))
    pi_w=(w[0] * pi,w[1] * pi)
    print(pi_w)
    draw(*[Arrow(w),Arrow(pi_w)])

def scale(s, v):
    return [s*elmt for elmt in v]
def A2_17():
    print(scale(3, (1,2)))

def A2_18():
    print("c = sqrt(a**2 + b**2)")
    print("s * (a, b) = (s*a, s*b)")
    print("sqrt((s*a)**2, (s*b)**2) = sqrt(s**2 * (a**2 + b**2)) = s * sqrt(a**2, b**2) = s * c")

def A2_19():
    print("(-4~4, -4~4)?")

def A2_20():
    print("|(a,b)| = sqrt(a**2 + b**2)")
    print("|(-a,-b) = sqrt((-a)**2 + (-b)**2)")
    print("(-a)**2 = a**2, (-b)**2 = b**2, sqrt((-a)**2 + (-b)**2) = sqrt(a**2 + b**2)")

def A2_21():
    print("v3과 v7")

def A2_22():
    print((0,0))

def A2_23():
    print("v-w=(-2.5,0.5)")
    print("u-v=(-3.5,-1.5)")
    print("w-v=(2.5,-0.5)")

def subtract(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1])
def A2_24():
    print(subtract((3,4), (1,3)))

def distance(v1, v2):
    return length(subtract(v1, v2))
def perimeter(vectors):
    return sum([distance(vectors[i], vectors[i+1])for i in range(0, len(vectors)-1)]) + distance(vectors[len(vectors) - 1], vectors[0])    
def A2_25():
    print(distance((3,4), (1,3)))
    print(perimeter(dino_vectors))

def A2_26():
    for n in range(1, 14):
        for m in range(1, n):
            if(distance((n,m), (1,-1)) == 13):
               print ("(", n-1, ",", m-(-1), ")")

def A2_27():
    print(distance((0,0), (-1.34,2.68)))

def A2_28():
    print(2/5)

def A2_29():
    print(f"x성분: ({15 * cos(37/180 * pi)},0)")
    print(f"y성분: (0,{15 * sin(37/180 * pi)})")
    
def A2_30():
    point = (8.5 * -0.574, 8.5*0.819)
    print(f"({point[0]},{point[1]})")
    draw(Arrow(point))

def A2_31():
    print("sin(0): 0")
    print("sin(1/2pi): 1")
    print("sin(1pi): 0")
    print("cos(0): 1")
    print("cos(1/2pi): 0")
    print("cos(1pi): -1")

def A2_32():
    print(f"{(1/2)**2+(sqrt(3)/2)**2} = {1**2}")
    print(f"sin(30degree) is {(1/2)/1}")
    print(f"cos(30degree) is {(sqrt(3)/2)/1}")
    print(f"tan(30degree) is {(1/2)/(sqrt(3)/2)}")

def A2_33():
    print(f"sin(60degree) is {(sqrt(3)/2)/1}")
    print(f"cos(60degree) is {(1/2)/1}")
    print(f"tan(60degree) is {(sqrt(3)/2)/(1/2)}")

def A2_34():
    print("0.648 = 0.643/1")
    print(f"a**2+b**2=C**2, 0.643**2+b**2=1**2, b**2=1-0.643**2, b={sqrt(1-0.643**2)}")
    b=sqrt(1-0.643**2)
    print(f"sin(50degree)={b/1}")
    print(f"tan(50degree)={b/0.643}")

def A2_35():
    print("180 degree=pi radian, 1 degree= 1/180 pi radian")
    print(f"116.57 degree=116.67/180*pi radian={116.57/180*pi} radian")
    print(f"tan({116.57/180*pi})={tan(116.57/180*pi)}")

def A2_36():
    print("10/6*180 degree={10/6*180} degree, 4 사분면")
    print(f"cos(10pi/6)=positive number={cos(10*pi/6)}")
    print(f"sin(10pi/6)=negative number={sin(10*pi/6)}")

def my_to_cartesian(p):
    return (p[0] * cos(p[1]), p[0] * sin(p[1]))

def A2_37():
    polars=[(cos(5*x*pi/500.0), 2*pi*x/1000.0) for x in range(0, 1001)]
    descartes=[my_to_cartesian(elmt) for elmt in polars]
    segments=[Segment(descartes[i], descartes[i+1]) for i in range(0, len(descartes)-1)]
    draw(*segments)

def A2_38():
    print(f"atan(y,x)={atan2(3,-2)}")

def A2_39():
    print("(-3)/2 = 3/(-2)")
    print(f"atan(3/-2)={atan(3/-2)}")

def A2_40():
    print("(sqrt(2), 45/180*pi), (sqrt(2), -45/180*pi)")
    print(f"({sqrt(2)}, {45/180*pi}), ({sqrt(2)}, {-45/180*pi})")
    print(f"{to_polar((1,1))}, {to_polar((1,-1))}")

def to_positive_angle(polar):
    if(polar[1] < 0):
        return (polar[0], polar[1]%(-2*pi)+(2*pi))
    else:
        return (polar[0], polar[1]%(2*pi))
def A2_41():
    mouth1=to_positive_angle(to_polar(subtract((-5,2),(-2,2))))
    mouth2=to_positive_angle(to_polar(subtract((-5,1),(-2,2))))
    tail1=to_positive_angle(to_polar(subtract((3,1),(6,4))))
    tail2=to_positive_angle(to_polar(subtract((5,1),(6,4))))
    foot1=to_positive_angle(to_polar(subtract((0,-3),(-1,-4))))
    foot2=to_positive_angle(to_polar(subtract((1,-4),(-1,-4))))

    print(f"mouth={abs(mouth1[1]-mouth2[1])*180/pi}")
    print(f"tail={abs(tail1[1]-tail2[1])*180/pi}")
    print(f"foot={abs(foot1[1]-foot2[1])*180/pi}")

def rotate(angle, vectors):
    polars=[to_polar(vector) for vector in vectors]
    rotatedPolars=[(polar[0], polar[1]+angle) for polar in polars]
    return [to_cartesian(polar) for polar in rotatedPolars]
def A2_42():
    draw(Polygon(*dino_vectors))
    draw(Polygon(*rotate(45/180*pi, dino_vectors)))
    draw(Polygon(*rotate(-45/180*pi, dino_vectors)))
    
def regular_polygon(n):
    angleStep=2*pi/n
    return [to_cartesian((1, angleStep * i)) for i in range(0, n)]
def A2_43():
    regularPolygon = regular_polygon(7)
    draw(Points(*regularPolygon), Polygon(*regular_polygon(7)))

def A2_44():
    transitionRotation=Polygon(*rotate(5/3*pi, [add([vector, (8,8)]) for vector in dino_vectors]))
    rotationTransition=Polygon(*[add([vector, (8,8)]) for vector in rotate(5/3*pi, dino_vectors)])
    draw(transitionRotation, rotationTransition)



#A2_1()
#A2_2()
#A2_3()
#A2_4()
#A2_5()
#A2_6()
#A2_7()
#A2_8()
#A2_9()
#A2_10()
#A2_11()
#A2_12()
#A2_13()
#A2_14()
#A2_15()
#A2_16()
#A2_17()
#A2_18()
#A2_19()
#A2_20()
#A2_21()
#A2_22()
#A2_23()
#A2_24()
#A2_25()
#A2_26()
#A2_27()
#A2_28()
#A2_29()
#A2_30()
#A2_31()
#A2_32()
#A2_33()
#A2_34()
#A2_35()
#A2_36()
#A2_37()
#A2_38()
#A2_39()
#A2_40()
#A2_41()
#A2_42()
#A2_43()
#A2_44()