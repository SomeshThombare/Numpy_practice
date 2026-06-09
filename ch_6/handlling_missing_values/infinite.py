import numpy as np

arr = np.array([1,2, np.inf, 4, -np.inf, 6,7, np.inf])

print(np.isinf(arr))