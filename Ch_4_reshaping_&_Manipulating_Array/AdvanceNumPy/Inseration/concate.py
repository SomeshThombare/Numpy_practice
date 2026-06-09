import numpy as np

arr = np.array([10,20,40,50])
print(arr)

arr1 = np.array([60,70,80])
print(arr1)

new_arr = np.concatenate((arr,arr1))
print(new_arr)

