from vector_drawing import *

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
    print("x성분: ", added[0])
    print("y성분: ", added[1])
    length = sqrt(added[0]**2 + added[1]**2)
    print("길이: ", length)

def Length(vector):
    return sqrt(vector[0]**2 + vector[1]**2)
def A2_14():
    print("작성 중...")


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
