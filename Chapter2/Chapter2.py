from vector_drawing import *
from math import sin
from math import cos
from math import tan

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
A2_30()
A2_31()