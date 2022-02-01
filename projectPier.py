from cmath import pi
from operator import le
from re import L
from anyio import current_default_worker_thread_limiter
from matplotlib.pyplot import legend
import numpy as np
import matplotlib.pylab as plt
from sympy import rad

sheet_dimension = 3000

length_a = 1000
length_b = 1500
radius = 100

coeff = 0.5

timesteps = np.linspace(0,100, num = 150)


def background(sheet_dimension):
    back = np.zeros((sheet_dimension,sheet_dimension))
    return back

def rectangle(x,y):
    return np.ones((y,x))

def circle(radius_out, radius_in = 0):
    x = np.linspace(-radius_out,radius_out, 2*radius_out)
    y = np.linspace(-radius_out,radius_out, 2*radius_out)
    A = np.zeros((2*radius_out,2*radius_out))
    for i in x[:-1]:
        for j in y[:-1]:
            r = np.sqrt(i**2+j**2)
            if r < radius_out and r >= radius_in:  
                A[radius_out+int(i),radius_out+int(j)] = 1
    figure = A
    return figure

def ellipse(a_max, b_max, a_min = 0, b_min = 0):
    x = np.linspace(-a_max,a_max, num = 2*a_max)
    y = np.linspace(-b_max,b_max, num = 2*b_max)
    A = np.zeros((2*a_max+1,2*b_max+1))

    for i in x:
        for j in y:
            r_max = np.sqrt(i**2/a_max**2+j**2/b_max**2)
            r_min = np.sqrt(i**2/a_min**2+j**2/b_min**2)
            if r_max < 1 and r_min > 1:  
                A[a_max+int(i),b_max+int(j)] = 1
            else:
                A[a_max+int(i),b_max+int(j)] = 0
    figure = A
    return figure

def apply_figure(background, figure_to_apply, x_coordinate = 0, y_coordinate = 0):
    N = int(np.size(background[:,0]))
    a = int(np.size(figure_to_apply[:,0])/2)
    b = int(np.size(figure_to_apply[0,:])/2)

    x_start = int(N/2 + x_coordinate)
    y_start = int(N/2 + y_coordinate)

    background[(y_start-a):(y_start+a),(x_start-b):(x_start+b)] = figure_to_apply
    new_figure = background
    return new_figure

    
back = background(sheet_dimension)

central_rect = coeff*rectangle(length_b-2*radius,length_a-2*radius)
orizontal = coeff*rectangle(length_b-2*radius,radius)
vertical = coeff*rectangle(radius,length_a-2*radius)
cir = coeff*circle(radius)
ellip = coeff*ellipse(100,50,90,40)

for i in [-1,1]:
    for j in [-1,1]:
        picture = apply_figure(back,cir,i*length_b/2-i*radius,j*length_a/2-j*radius)

picture = apply_figure(back, central_rect,0,0)
picture = apply_figure(back,orizontal,0,length_a/2-radius/2)
picture = apply_figure(back,orizontal,0,-length_a/2+radius/2)
picture = apply_figure(back,vertical,length_b/2-radius/2,0)
picture = apply_figure(back,vertical,-length_b/2+radius/2,0)



figure, axes = plt.subplots()

axes.imshow(picture)

plt.show()

