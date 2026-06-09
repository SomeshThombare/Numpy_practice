#converitng a one array type to another type array i.e 1D to 2D
import numpy as np

arr = np.array([10,20,30,40,50,60])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
"""[[10 20 30]
 [40 50 60]]"""

reshaped_arr = arr.reshape(3,2)
print(reshaped_arr)
