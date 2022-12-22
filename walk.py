import numpy as np

# Array of probabilities
A = np.array([[0.2, 0.6, 0.2], 
			  [0.3, 0.0, 0.7],
			  [0.5, 0.0, 0.5]])

# Each value is the transition probability between the row and column index.

# (Iteration is slow, keep the amount of steps relatively low)
steps = 15

states = {0: '1', 1: '2', 2: '3'}
start = 0

# First iteration
print(states[start], "--->", end=" ")
prev = start

while steps-1: # Already done first iteration
	curr = np.random.choice(list(states.keys()), p=A[prev])
	print(states[curr], "--->", end=" ")
	prev = curr
	steps -= 1