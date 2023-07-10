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







