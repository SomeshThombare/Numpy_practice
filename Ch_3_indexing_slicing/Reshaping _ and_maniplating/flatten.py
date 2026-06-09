import numpy as np
"""
.ravel() --> view
.flatten() --> copy
"""
arr = np.array([[10,20,30],[40,50,60]])
print(arr.ravel())
print("--------------------")
print(arr.flatten())

