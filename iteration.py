import numpy as np

# Transition matrix
A = np.array([[0.2, 0.6, 0.2], 
			  [0.3, 0.0, 0.7],
			  [0.5, 0.0, 0.5]])

# Each value is the transition probability between the row and column index.

# (Iteration is slow, keep the amount of steps relatively low)
steps = 10**6

states = {0: '1', 1: '2', 2: '3'}
start = 0

# Stationary probabilities
pi = np.array([0, 0, 0])

# First iteration
pi[start] += 1
prev = start

i = 0
while i < steps:
	curr = np.random.choice(list(states.keys()), p=A[prev])
	pi[curr] += 1
	prev = curr
	i += 1

# Divide the frequencies for each state by the amount of steps
# to find the stationary probabilities
print("π =", pi/steps)