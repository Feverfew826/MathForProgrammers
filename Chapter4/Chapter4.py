from vectors import *
from teapot import *
from draw_model import *

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

#A1()
#A2()
A3()