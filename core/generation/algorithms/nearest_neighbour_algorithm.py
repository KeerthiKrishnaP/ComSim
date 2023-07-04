import math
import random

import numpy as np


def NNA(Xc, Yc, Rc, IFD, rmax, Acc_fibers, L_RVE):
    fiber_found = 0
    attempt = 1
    max_attempts = 10
    temp_R = rmax
    temp_IFD = IFD
    theta = 0
    while fiber_found == 0:
        theta = theta + random.randint(0, 5)
        d = Rc + temp_R + 1.01 * temp_IFD 
        (temp_X, temp_Y) = Find_center(Xc, Yc, d, theta)
        fiber_found = compatability_check(
            temp_X, temp_Y, temp_R, L_RVE, Acc_fibers, temp_IFD, rmax, fiber_found
        )
        if fiber_found == 1:
            Xn = temp_X
            Yn = temp_Y
            Rn = temp_R
            attempt = attempt + 1
            break
        else:
            attempt = attempt + 1
        if attempt > max_attempts:
            Xn = temp_X
            Yn = temp_Y
            Rn = temp_R
            fiber_found = 0
            break
    return (Xn, Yn, Rn, fiber_found)



def Find_center(Xc, Yc, d, theta):
    temp_X = Xc - d * np.cos(theta)  # theta input in degrees
    temp_Y = Yc - d * np.sin(theta)
    return (temp_X, temp_Y)




# Input data
rmax = 10
rmin = [5, 6, 7, 8, 9]
points = [6, 8, 10, 12, 14]
# packing the circles
delta = 20
L_RVE = rmax * delta
Vf = 30
#
x_min, x_max = 0, 2 * math.pi
my_dpi = 96
n_pixels = 800
figure_name = "circles.jpg"

# Main
# Packing cricles
Acc_fibers = circlebased(rmax, L_RVE, Vf)
# Plotting cricles
plot_circles(
    [i[0] for i in Acc_fibers],
    [i[1] for i in Acc_fibers],
    [i[2] for i in Acc_fibers],
    L_RVE,
    my_dpi,
    n_pixels,
    figure_name,
    reference_indices=[],
)
# Cal packinf fractions
Packing_Circles = cal_volumefraction_image(figure_name, n_pixels)
print("Packing fraction of Circles", Packing_Circles)
