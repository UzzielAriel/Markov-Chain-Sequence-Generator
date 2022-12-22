import numpy as np

# Transition matrix
A = np.array([[0.2, 0.6, 0.2], 
			  [0.3, 0.0, 0.7],
			  [0.5, 0.0, 0.5]])

# Each value is the transition probability between the row and column index.

# Much faster method, larger steps will work.
steps = 10**7

# An = A^n (n being steps)
An = A

i = 0
while i < steps:
	An = np.matmul(An, A)
	i += 1

# print(f"A^n = \n{An}\n")
print(f"π = {An[0]}")