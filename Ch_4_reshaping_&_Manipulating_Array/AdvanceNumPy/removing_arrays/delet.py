import numpy as np

arr = np.array([10,20,30,40,50])
print(arr)

new_arr = np.delete(arr,0)
print(new_arr)

new_2d_arr = np.array([[1,2,3],[4,5,6]])
print(new_2d_arr)

new_2d_arr1 = np.delete(new_2d_arr,0,axis=0)
print(f"after deleted{new_2d_arr1}")
"""after deleted[[4 5 6]]"""
