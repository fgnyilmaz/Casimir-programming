from operator import le
from re import L
from matplotlib.pyplot import legend
import numpy as np
import matplotlib.pylab as plt

sheet_dimension = 300

length_a = 100
length_b = 150
radius = 10


def background(sheet_dimension):
    back = np.zeros((sheet_dimension,sheet_dimension))
    return back
    

def inner_rectange(length_a, length_b, radius):
    new_a = length_a - 2*radius
    new_b = length_b - 2*radius

    rectangle = np.ones((new_a,new_b))
    return rectangle

def outer_vertical_rect(length_a,radius):
    new_a = length_a - 2*radius
    c = radius

    rectangle = np.ones((new_a,c))

    return(rectangle)

def outer_orizontal_rect(length_b,radius):
    new_b = length_b - 2*radius
    c = radius

    rectangle = np.ones((c,new_b))

    return(rectangle)

def apply_central_rectagle(background, rectangle):
    N = np.size(background[:,0])
    x = np.size(rectangle[:,0])
    y = np.size(rectangle[0,:])

    
    

    if N % 2 != 0:
        N = N+1
    if y % 2 != 0:
        y = y+1
    if x % 2 != 0:
        x = x+1

    background[int((N/2)-(x/2)):int((N/2)+(x/2)),int((N/2)-(y/2)):int((N/2)+(y/2))] = rectangle
    figure = background
    return figure

def apply_lateral_rectangles(background, orizontal, vertical):
    N = np.size(background[:,0])
    x = np.size(orizontal[0,:])
    y = np.size(vertical[:,0])
    r = np.size(orizontal[:,0])


    if N % 2 != 0:
        N = N+1
    if y % 2 != 0:
        y = y+1
    if x % 2 != 0:
        x = x+1
    if r % 2 != 0:
        r = r+1


    background[int(N/2-y/2):int(N/2+y/2),int(N/2-x/2-r):int(N/2-x/2)] = vertical
    background[int(N/2-y/2):int(N/2+y/2),int(N/2+x/2):int(N/2+x/2+r)] = vertical

    background[int(N/2-y/2-r):int(N/2-y/2),int(N/2-x/2):int(N/2+x/2)] = orizontal
    background[int(N/2+y/2):int(N/2+y/2+r),int(N/2-x/2):int(N/2+x/2)] = orizontal

    figure = background
    return figure




back = background(sheet_dimension)
central_rect = inner_rectange(length_a,length_b,radius)
orizontal = outer_orizontal_rect(length_b,radius)
vertical = outer_vertical_rect(length_a,radius)


picture = apply_central_rectagle(back,central_rect)
picture = apply_lateral_rectangles(back,orizontal,vertical)

figure, axes = plt.subplots()

axes.imshow(picture)

plt.show()

