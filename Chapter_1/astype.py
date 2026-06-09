#change the one data type into another datatype
import numpy as np

arr = np.array([10,20,30,40])
print(arr.dtype)

float_arr = arr.astype(float)
print(float_arr)

str_arr = arr.astype(str)
print(str_arr)
