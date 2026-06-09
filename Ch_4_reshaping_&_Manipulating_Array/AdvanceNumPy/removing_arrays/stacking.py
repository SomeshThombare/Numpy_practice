import numpy as np

"""
vertically--> vstack() row wise
horizontally -->hstask() column wise
"""

arr1 = np.array([10,20,30])

arr2 = np.array([40,50,60])

print(np.vstack((arr1,arr2)))#verticalllly
"""[[10 20 30]
 [40 50 60]]"""

print(np.hstack(((arr1,arr2))))#horizontally
"""[10 20 30 40 50 60]"""