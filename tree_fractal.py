import numpy as np
import matplotlib.pyplot as plt

depth = 8               # Number of iterations
angle = np.pi/9         # Deviation between root and branch
scale = 0.7             # Scaling factor for branch length

# Draw a line between points
def line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], 'k', linewidth=1)

# Rotate P1 about P0 by angle
def rotate(x1, y1, x0, y0, angle):
    x1 -= x0
    y1 -= y0
    s, c = np.sin(angle), np.cos(angle)
    x2 = x1 * c - y1 * s
    y2 = x1 * s + y1 * c
    return x2 + x0, y2 + y0

# Extend P0 in the direction given by angle
def extend(x0, y0, angle, length):
    s, c = np.sin(angle), np.cos(angle)
    x1, y1 = length * c, length * s
    return x1 + x0, y1 + y0

# Draw a branch at P0 at angle 'a', length 'l'
def branch(x0, y0, a, l, d=0):
    x1, y1 = extend(x0, y0, a, l)
    line(x0, y0, x1, y1)
    # Recurse if maximum depth not reached
    if d < depth:
        # Draw branches to the left and right
        branch(x1, y1, a + angle, l * scale, d + 1)
        branch(x1, y1, a - angle, l * scale, d + 1)

# Draw the root
branch(0, 0, np.pi/2, 1)

plt.gca().set_aspect('equal', adjustable='box')
# plt.show()
plt.savefig('tree.png')
