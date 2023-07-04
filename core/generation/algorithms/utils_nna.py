import random

import numpy as np


def add_new_fiber_nna(rmax, L_RVE, Vf):
    IFD = 0.01 * rmax

    fn = 1
    X = random.randint(0, L_RVE)
    Y = random.randint(0, L_RVE)
    R = rmax
    Acc_fibers = np.empty((0, 3))
    Acc_fibers = np.append(Acc_fibers, np.array([[X, Y, R]]), axis=0)
    while fn <= 105:
        fiber_found = 0
        if fn == 1:
            Xc = X
            Yc = Y
            Rc = R
            # Subscripit C represnts the center fiber to pack next fibers
            (Xn, Yn, Rn, fiber_found) = NNA(
                Xc, Yc, Rc, IFD, rmax, Acc_fibers, L_RVE
            )  # new fibers provided by the NNA
            Acc_fibers = np.append(Acc_fibers, np.array([[Xn, Yn, Rn]]), axis=0)
            fn = fn + 1
        else:
            while fiber_found == 0:
                for j in range(0, len(Acc_fibers)):
                    Xc = Acc_fibers[j][0]
                    Yc = Acc_fibers[j][1]
                    Rc = Acc_fibers[j][2]
                    (Xn, Yn, Rn, fiber_found) = NNA(
                        Xc, Yc, Rc, IFD, rmax, Acc_fibers, L_RVE
                    )
                    if fiber_found == 1:
                        Acc_fibers = np.append(
                            Acc_fibers, np.array([[Xn, Yn, Rn]]), axis=0
                        )
                        fn = fn + 1
                        break
    return Acc_fibers


def Find_center(Xc, Yc, d, theta):
    temp_X = Xc - d * np.cos(theta)
    temp_Y = Yc - d * np.sin(theta)
    return (temp_X, temp_Y)
