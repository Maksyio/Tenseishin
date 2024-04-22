import numpy as np
import scipy as sp

# Define the number of points in each direction
n_p = 10

def CreatePoints(n_p):
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

def Init_Field(all_points):
    associated_arrays = []
    for point in all_points:
        # Calculate the magnitude from the coordinates of the point
        magnitude = np.linalg.norm([point['x'], point['y'], point['z']])
        
        # Create an associated array for each point
        associated_array = np.array(dtype=[('m', float, 3)], dtype=[('d', float, 3)])
        associated_arrays.append(associated_array)
    return associated_arrays



# Generate all_points
all_points = CreatePoints(n_p)

# Create associated arrays for each point in all_points
associated_arrays = Init_Field(all_points)

# Example usage:
for point, associated_array in zip(all_points, associated_arrays):
    print("Point:", point)
    print("Associated Array:", associated_array)

# Define Electric Field
# def E_field(Charge):
#    for point in all_points:
