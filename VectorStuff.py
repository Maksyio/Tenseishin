import numpy as np
import scipy as sp
# from manim import * # add this in once you have an understanding of the code

#consider 3D space in cartesian co-ordinates
#each point can be considered to have an associated vector, which represents the magnitude and direction of a field that acts apon it.
#this can be achieved by creating a 3D array of vectors


#the number of points we want to consider has to be defined prior to the space vector
n_p = 10 # therefore if we consider 10 points in each direction, the space vector will in total have 1000 points

#3D space vector
X = np.zeros((n_p, 1), dtype=float)
Y = np.zeros((n_p, 1), dtype=float)
Z = np.zeros((n_p, 1), dtype=float)
Space = np.array([X,Y,Z])

print(Space)