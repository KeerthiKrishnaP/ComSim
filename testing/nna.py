import math

from core.generation.algorithms import nearest_neighbour_algorithm

rmax = 10
rmin = [5, 6, 7, 8, 9]
points = [6, 8, 10, 12, 14]
delta = 20
L_RVE = rmax * delta
Vf = 30
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
