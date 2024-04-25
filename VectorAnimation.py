import numpy as np
from manim import *

import numpy as np

# Define the number of points in each direction
n_p = 10

def Create(n_p):
    # Define X, Y, and Z arrays for the positive octant (1st octant)
    X_positive = np.arange(0, n_p)
    Y_positive = np.arange(0, n_p)
    Z_positive = np.arange(0, n_p)

    # Create meshgrid for the positive octant
    XX_positive, YY_positive, ZZ_positive = np.meshgrid(X_positive, Y_positive, Z_positive, indexing='ij')

    # Combine coordinates into a structured array for the positive octant
    positive_points = np.empty((len(X_positive)*len(Y_positive)*len(Z_positive),), dtype=[('x', float), ('y', float), ('z', float)])
    positive_points['x'] = XX_positive.ravel()
    positive_points['y'] = YY_positive.ravel()
    positive_points['z'] = ZZ_positive.ravel()

    # Define X, Y, and Z arrays for the negative octant (8th octant)
    X_negative = -np.arange(1, n_p)
    Y_negative = -np.arange(1, n_p)
    Z_negative = -np.arange(1, n_p)

    #   Create meshgrid for the negative octant
    XX_negative, YY_negative, ZZ_negative = np.meshgrid(X_negative, Y_negative, Z_negative, indexing='ij')

    # Combine coordinates into a structured array for the negative octant
    negative_points = np.empty((len(X_negative)*len(Y_negative)*len(Z_negative),), dtype=[('x', float), ('y', float), ('z', float)])
    negative_points['x'] = XX_negative.ravel()
    negative_points['y'] = YY_negative.ravel()
    negative_points['z'] = ZZ_negative.ravel()

    # Concatenate positive and negative octants together
    all_points = np.concatenate((positive_points, negative_points))
    return all_points

def Initialise(array):
    p_arrays = []
    for point in array:
        # Calculate the magnitude from the coordinates of the point
        direction = np.array([0, 0, 0])
        magnitude = 0
        # Create an associated array for each point with magnitude included
        p_array = np.array([(direction, magnitude)], dtype=[('d', float, 3), ('magnitude', float)])
        p_arrays.append(p_array)
    return p_arrays

def E_Field(Q, x, points, p_arrays):
    # Convert x to a NumPy array
    x = np.array(x)
    for point, p_array in zip(points, p_arrays):
        # Convert point to a tuple or list
        point_tuple = (point['x'], point['y'], point['z'])
        # Calculate the vector between the charge Q and q
        r = x - np.array(point_tuple)
        # Calculate the magnitude and direction only if r is non-zero
        if np.linalg.norm(r) != 0:
            magnitude = 1/(4 * np.pi * 35.4167 * 0.000000000001) * Q * 1/(np.linalg.norm(r)) ** 2
            direction = r/(np.linalg.norm(r))
        else:
            magnitude = 0
            direction = np.array([0, 0, 0])
        # Update the associated array for the current point
        p_array['d'] = direction
        p_array['magnitude'] = magnitude
        #introduce an if statement, so that, if all vectors are extremely large or extremely small, they will be reduced/increased to a reasonable size
    return p_arrays

def position(dt, t_interval):
    positions = []
    p_initial = (0, 0, -10)
    p_final = (0, 0, 10)
    
    # Calculate the displacement between p_initial and p_final
    displacement = tuple((f - i) / (t_interval / dt) for i, f in zip(p_initial, p_final))
    
    # Generate positions at regular intervals
    for i in range(int(t_interval / dt) + 1):
        x = p_initial[0] + displacement[0] * i
        y = p_initial[1] + displacement[1] * i
        z = p_initial[2] + displacement[2] * i
        positions.append((x, y, z))
    
    return positions
#define a new function that will use both functions E_field() and Position() to generate a new set of data for every dt - think about how to optimise this function to not take up lots of space

def update_E_Field(dt, positions, points, p_arrays):
    for position in positions:
        vector = position
        p_arrays = E_Field(1, [vector], points, p_arrays)
    return p_arrays

def save_to_file(filename, points, p_arrays):
    with open(filename, 'a') as file:  # Append mode to add data for each time step
        for point, p_array in zip(points, p_arrays):
            file.write("Point: {}\n".format(point))
            file.write("Point Data: {}\n".format(p_array))
        file.write("\n")  # Add a newline to separate data for each time step

class ElectricFieldAnimation(ThreeDScene):
    def construct(self):

        def read_data(self, filename):
            # Implement code to read data from the file
            pass

        def create_objects(self, points, p_arrays):
            # Implement code to create Manim objects based on the data
            pass
        # Define variables
        dt = 0.01  # Time step
        t_interval = 10  # Total time interval
        filename_base = 'FieldAroundElectron_'  # Base filename

        # Loop through each frame
        for t in np.arange(0, t_interval, dt):
            # Generate filename for the current frame
            filename = filename_base + str(round(t, 2)) + '.txt'
            
            # Read data from the current file
            points, p_arrays = read_data(filename)
            
            # Create Manim objects based on the data
            objects = create_objects(points, p_arrays)
            
            # Add objects to the scene
            self.add(*objects)
            
            # Wait for dt seconds before moving to the next frame
            self.wait(dt)

