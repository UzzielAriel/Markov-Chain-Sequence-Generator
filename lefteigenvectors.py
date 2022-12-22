import scipy.linalg
import numpy as np

# Transition matrix
A = np.array([[0.2, 0.6, 0.2], 
			  [0.3, 0.0, 0.7],
			  [0.5, 0.0, 0.5]])

# Each value is the transition probability between the row and column index.

eigenValues, eigenVectors = scipy.linalg.eig(A, right = False, left = True)

# print(f"Left eigen vectors = \n{eigenVectors}\n")
# print(f"Eigen values = {eigenValues}")

# Take only non-complex column vector
pi = eigenVectors[:, 0]

# Find quotient of sum of non-complex eigenvector with each value
pi = [(v/np.sum(pi)).real for v in pi]

print(f"π = {pi}")