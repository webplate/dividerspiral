"""Simple matshow() example."""
import matplotlib.pyplot as plt
import numpy as np
from sympy.ntheory import factorint
import scipy.misc
import colormaps as cmaps
import Image

def spiral_coord(dim):
    '''compute coordinates along ulam's spiral'''
    coords = []
    c = dim/2
    xo = 0
    yo = 0
    n = 1
    for l in range(c):
        # go right
        while yo < l:
            coords.append((xo+c, yo+c, n))
            yo += 1
            n += 1
        # go up
        while xo > -l:
            coords.append((xo+c, yo+c, n))
            xo -= 1
            n += 1
        # go left
        while yo > -l:
            coords.append((xo+c, yo+c, n))
            yo -= 1
            n += 1
        # go down
        while xo < l:
            coords.append((xo+c, yo+c, n))
            xo += 1
            n += 1
    return coords

def divider_mat_sympy(dim):
    '''ulam's spiral showing number of divisers'''
    aa = np.zeros((dim, dim))
    for coord in spiral_coord(dim):
        i, j, n = coord
        # compute nb of divisers
        f = factorint(n)
        nb_div = 1
        for p in f:
            nb_div *= f[p] + 1
        aa[i, j] = nb_div
    return aa

def spiral_mat(dim):
    bb = np.zeros((dim, dim))
    for coord in spiral_coord(dim):
        i, j, n = coord
        bb[i, j] = n
    return bb

size = 1024
cmap = cmaps.viridis
cmap.set_under('#000000')
#~ plt.matshow(spiral_mat(size), cmap=cmap)
mat = divider_mat_sympy(size)
#~ plt.matshow(mat, cmap=cmap, vmin=3)

# save bitmap with colormap
normalized = mat / np.max(mat)
im = Image.fromarray(np.uint8(cmap(normalized)*255))
im.save('spiral.png')


#~ plt.show()
