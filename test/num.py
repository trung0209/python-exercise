import numpy as np
M = np.array([[0, 1, 0, 0],
              [1, 0, 0, 0],
              [0,0, 0, 1],
              [0, 0, 1, 0]])
# vals, vecs = np.linalg.eig(M)
# vecs

# Eigenvalues
b = np.array([[0.1,0.1, 0.1,  0.7],
              [ 0.7, 0.1, 0.1, 0.1],
              [0.1,  0.7, 0.1,0.1],
              [0.1,0.1, 0.7, 0.1]])
# vals, vecs = np.linalg.eig(b)
# vals

c = np.array([[3/2, -1],
              [-1/2, 1/2]]
              )
vals, vecs = np.linalg.eig(c)
print()
print(vecs)
