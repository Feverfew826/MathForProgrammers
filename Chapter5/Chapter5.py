from transforms import *
from transforms import rotate_z_by
from math import pi
import numpy.random
from draw_model import *
from teapot import *

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
A15()
