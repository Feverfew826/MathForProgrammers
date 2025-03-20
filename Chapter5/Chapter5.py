from transforms import *
from transforms import rotate_z_by
from math import pi
import numpy.random
from draw_model import *
from teapot import *
from draw3d import *

def infer_matrix(n, transformation):
    return zip(*[transformation(tuple([1 if n1==n2 else 0 for n2 in range(0,n)])) for n1 in range(0, n)])

def A1():
    print(*infer_matrix(3,rotate_z_by(pi/2)))

def A2():
    print("(")
    print("(-3.04)")
    print("(-15.29)")
    print(")")

def matrix_multiply(a, b):
    return [tuple(dot(row, col) for col in zip(*b)) for row in a]
def random_matrix(n):
    return [tuple([numpy.random.randint(0, 10) for j in range(0, n)]) for i in range(0, n)]
def A3():
    first=random_matrix(3)
    second=random_matrix(3)
    print(first)
    print(second)
    print(matrix_multiply(first, second))

def A4():
    first=random_matrix(3)
    second=random_matrix(3)
    print(first)
    print(second)
    print(matrix_multiply(first, second))
    print(matrix_multiply(second, first))
    print("다르다.")

def A5():
    print("(")
    print("(1, 0)")
    print("(0, 1)")
    print(")")
    print("(")
    print("(1, 0, 0)")
    print("(0, 1, 0)")
    print("(0, 0, 1)")
    print(")")

def matrix_multiply_vector_by(mat):
    def newFuction(v):
        return multiply_matrix_vector(mat, v)
    return newFuction
def A6():
    u=(
        (2,1,1),
        (1,2,1),
        (1,1,2)
    )
    draw_model(load_triangles())
    draw_model(polygon_map(matrix_multiply_vector_by(u), load_triangles()))

def my_multiply_matrix_vector1(matrix, vector):
    return tuple(sum([x*y for x, y in zip(row, vector)]) for row in matrix)
def A7():
    randomMatrix = random_matrix(3)
    print(multiply_matrix_vector(randomMatrix, (4,7,2)))
    print(my_multiply_matrix_vector1(randomMatrix, (4,7,2)))

def my_multiply_matrix_vector2(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)
def A8():
    randomMatrix = random_matrix(3)
    print(multiply_matrix_vector(randomMatrix, (4,7,2)))
    print(my_multiply_matrix_vector2(randomMatrix, (4,7,2)))

# 연습장에 품...
def A9():
    print("전개해보면 알수 있음")

A=(
    (1,1,0),
    (1,0,1),
    (1,-1,1)
)
B=(
    (0,2,1),
    (0,1,0),
    (1,0,-1)
)
def compose_a_b(vector):
    return multiply_matrix_vector(A, multiply_matrix_vector(B, vector))
    
def A10():
    print(*infer_matrix(3, compose_a_b))
    print(matrix_multiply(A,B))

# 전혀 아니었음. 90도 회전, 270도 회전시키는 일차변환 벡터를 구해야함.
# x축 기저 벡터와 y축 기저 벡터에 임의의 행렬을 곱해서 회전한 결과가 되는지 확인하는 것으로
# 90도 회전시키는 행렬과, 270도 회전시키는 행렬을 구할 수 있음.
def A11():
    op0=(
        (sqrt(0.5),-sqrt(0.5)),
        (sqrt(0.5),sqrt(0.5)),
    )
    op1=(
        (sqrt(0.5),sqrt(0.5)),
        (-sqrt(0.5),sqrt(0.5)),
    )
    print(matrix_multiply(op0, op1))

def matrix_power(power, matrix):
    result=matrix
    for i in range(1, power):
        result=matrix_multiply(result, matrix)
    return result
def A12():
    print(matrix_power(1, A))
    print(matrix_power(2, A))
    print(matrix_power(3, A))
    # 검산
    print(A)
    print(matrix_multiply(A, A))
    print(matrix_multiply(matrix_multiply(A, A), A))

def A13():
    print("3x5")

def A14():
    print("2x1")
    print("1x2")
    print("3x1")
    print("1x3")

def ex_matrix_multiply(op0, op1):
    op0Col = len(op0[0])
    op1row = len(op1)
    if(op0Col != op1row):
        raise Exception(f"col-row not same. col: {op0Col}, row: {op1row}")
    return matrix_multiply(op0, op1)
def A15():
    print(ex_matrix_multiply(A,B))
    BadA=(
        (1,1),
        (1,0),
        (1,-1)
    )
    print(ex_matrix_multiply(BadA,B))

def A16():
    print("b, 2X2")
    print("c, 3X8")

def A17():
    print("5X3 행렬과 3X2 행렬을 곱할 수 잇으며, 5X2")

# 못 품
def transpose(vector):
    return;
def A18():
    transpose(((1, 2, 3),))
    transpose(((1,) (2,), (3,)))

# 연습장에 그림.
def A19():
    print("서로 어떻게 곱하려고 시도하던지 열의 수와 행의 수가 일치하지 않는다.")

def A20():
    print("2X3*3X5*5X7 순으로 곱할 수 있다. 결과 행렬의 크기는 2X7")

def A21():
    print("yz: ((0,1,0), (0,0,1))")
    print("xz: ((1,0,0), (0,0,1))")

# 못 품
def A22():
    return;

def A23():
    print("("
    "   (1, 1, 1, 1, 1),"
    "   (1, 0, 1, 1, 1),"
    "   (1, 1, 0, 1, 1),"
    "   (1, 1, 1, 0, 1),"
    ")")

def A24():
    print("("
    "   (0, 0, 0, 0, 0, 1),"
    "   (0, 0, 0, 1, 0, 0),"
    "   (1, 0, 0, 0, 0, 0),"
    "   (0, 1, 0, 0, 0, 0),"
    "   (0, 0, 1, 0, 0, 0),"
    "   (0, 0, 0, 0, 1, 0),"
    ")")

def A25():
    print("M*M, 3X3")
    print("N*N, 2X2")
    print("N*P, 2X3")
    print("N*Q, 2X3")
    print("P*M, 2X3")
    print("Q*M, 2X3")

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]
def polygon_segments_3d(points,color='blue'):
    count = len(points)
    return [Segment3D(points[i], points[(i+1) % count], color=color) for i in range(0, count)]
magic_matrix = (
    (1,0,3),
    (0,1,1),
    (0,0,1)
)
def A26():
    dino_3d = [(x,y,2) for x,y in dino_vectors]
    translated = [multiply_matrix_vector(magic_matrix, v) for v in dino_3d]
    draw3d(Points3D(*dino_3d, color='blue'), *polygon_segments_3d(dino_3d), Points3D(*translated, color='red'), *polygon_segments_3d(translated, 'red'))
    print("두 배 이동한다.")

def A27():
    matrix27 = (
        (1,0,-2),
        (0,1,-2),
        (0,0,1)
    )
    dino_3d = [(x,y,1) for x,y in dino_vectors]
    translated = [multiply_matrix_vector(matrix27, v) for v in dino_3d]
    draw3d(Points3D(*dino_3d, color='blue'), *polygon_segments_3d(dino_3d), Points3D(*translated, color='red'), *polygon_segments_3d(translated, 'red'))

def A28():
    print("전개하면 다음과 같이 되므로, z값이 유지된다.")
    print("("
        "(ax+by+cz,),"
        "(dx+ey+fz,),"
        "(0x+0y+1z,)"
    ")")

def A29():
    matrix29 = (
        (0.5*cos(pi/4),-0.5*cos(pi/4),2),
        (0.5*sin(pi/4),0.5*sin(pi/4),2),
        (0,0,1)
    )
    dino_3d = [(x,y,1) for x,y in dino_vectors]
    translated = [multiply_matrix_vector(matrix29, v) for v in dino_3d]
    draw3d(Points3D(*dino_3d, color='blue'), *polygon_segments_3d(dino_3d), Points3D(*translated, color='red'), *polygon_segments_3d(translated, 'red'))

def A30():
    matrix29 = (
        (0.5*cos(pi/4),-0.5*cos(pi/4),2),
        (0.5*sin(pi/4),0.5*sin(pi/4),2),
        (0,0,1)
    )
    matrix30 = (
        (0.5*cos(pi/4),-0.5*cos(pi/4),cos(pi/4)),
        (0.5*sin(pi/4),0.5*sin(pi/4),2*sin(pi/4)),
        (0,0,1)
    )
    dino_3d = [(x,y,1) for x,y in dino_vectors]
    translated29 = [multiply_matrix_vector(matrix29, v) for v in dino_3d]
    translated30 = [multiply_matrix_vector(matrix30, v) for v in dino_3d]
    draw3d(Points3D(*dino_3d, color='blue'), *polygon_segments_3d(dino_3d), Points3D(*translated29, color='red'), *polygon_segments_3d(translated29, 'red') ,Points3D(*translated30, color='black'), *polygon_segments_3d(translated30, 'black'))

def translate_4d(translation):
    def new_fuction(target):
        a,b,c,d = translation
        x,y,z,w = target
        matrix = (
            (1,0,0,0,a),
            (0,1,0,0,b),
            (0,0,1,0,c),
            (0,0,0,1,d),
            (0,0,0,0,1)
            )
        vector = (x, y, z, w, 1)
        x_out, y_out, z_out, w_out,_ = multiply_matrix_vector(matrix, vector)
        return (x_out, y_out, z_out, w_out)
    return new_fuction
def A31():
     print(translate_4d((1,2,3,4))((10,20,30,40)))

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
#A28()
#A29()
#A30()
A31()