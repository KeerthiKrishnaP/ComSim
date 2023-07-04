import math


def compatability_check(
    temp_X, temp_Y, temp_R, L_RVE, Acc_fibers, temp_IFD, rmax, fiber_found
):
    Tol = 0.75 * rmax
    Pass = 0
    if temp_X < -Tol or temp_Y < -Tol or temp_X >= L_RVE + Tol or temp_Y >= L_RVE + Tol:
        fiber_found = 0
    else:
        for i in range(len(Acc_fibers)):
            Xo = Acc_fibers[i][0]
            Yo = Acc_fibers[i][1]
            Ro = Acc_fibers[i][2]
            Distance = math.sqrt((Xo - temp_X) ** 2 + (Yo - temp_Y) ** 2)
            if Distance > Ro + temp_R + temp_IFD:
                Pass = Pass + 1
            else:
                fiber_found = 0
        fiber_found = 1 if Pass == len(Acc_fibers) else 0
    return fiber_found
