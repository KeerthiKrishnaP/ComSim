import matplotlib.pyplot as plt
import numpy as np

# Input
R_mean = 0.00795  # mean fiber radius
delta = 40  # To determine the length of microstructure (L=Rf x delta)
UL = R_mean * delta  # Length of RVE UL upper limit
LL = 0.0  # Lower Limit origin
Rf = 0.019  # radius of fiber in case of constant fiber radius
P = 0  # Initiation of packing fraction
STD = 0.000  # Standard deviation of fiber radius
r = R_mean
Resolution = 0.0001  # Resolution of the image to calculate the packing fraction
file_name = 'Vf-20-Delta-40.txt'

# Packing parameter
target_Fiber_fraction = 0.20  # targeted packing fraction

# plot background
bx = np.array([LL, UL, UL, LL])  # X co-ordinates of the RVE
by = np.array([LL, LL, UL, UL])  # Y co-ordinates of the RVE
AP = UL * UL  # Area of area (Area of Polygon)
B = np.array(list(zip(bx, by)))  # Makes the convex hull in this case a square
plt.plot(bx, by, '.')  # Plots the polygon
plt.axis('equal')
plt.hold(True)
plt.fill(B[:, 0], B[:, 1], 'k', alpha=0.5)  # Color code for polygon

plt.show()
